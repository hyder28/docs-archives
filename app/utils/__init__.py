from .audio_process import *
from .file_process import *
from .constants import *
from .verify_torch import *

from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import librosa
import torch

import spacy
from spacy.matcher import PhraseMatcher
import pysbd

import collections

torch_device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


class SpacySM:
    """spacy en-core-web-sm-3.4.0"""

    def __init__(self):
        self.nlp = spacy.load(spacy_model_dir)
        self.matcher = PhraseMatcher(self.nlp.vocab)
        self.seg = pysbd.Segmenter(language = "en", clean = True)

    def get_topic(self, text_content):
        try:
            for label_class, keyword_list in keywords_lookup.items():
                patterns = [self.nlp.make_doc(term) for term in keyword_list] + [self.nlp.make_doc(term.lower()) for
                                                                                 term in keyword_list]
                self.matcher.add(label_class, patterns)

            sents_list = self.seg.segment(text_content)

            tagged_keywords = []
            for sent in sents_list:
                if 0 < len(sent) < self.nlp.max_length:
                    doc = self.nlp(sent)
                    matches = self.matcher(doc)

                    for match_id, start, end in matches:
                        rule_id = self.nlp.vocab.strings[match_id]
                        span = doc[start:end]

                        tagged_keywords.append((rule_id, span.text))

            ctr = dict(collections.Counter(tagged_keywords).most_common(3))

            return {"ARTICLE_TOPIC": str(ctr), "ARTICLE_TEXT": text_content}
        except Exception as e:
            logging.error(f"> error in text topic extraction: {e}")
            return {}


class Wav2Vec2:
    """wav2vec2 for asr"""

    def __init__(self):
        self.tokenizer = Wav2Vec2Tokenizer.from_pretrained(wav2vec2_model_dir, local_files_only=True)
        self.model = Wav2Vec2ForCTC.from_pretrained(wav2vec2_model_dir, local_files_only=True).to(torch_device)

    def transcribe_text(self, input_fpath, temp_dir_name = temp_folder):
        clear_files_in_folder()

        # audio files processing
        create_audio_chunks(input_fpath)

        fpath_list = os.listdir(temp_dir_name)
        fpath_list_sorted = sorted(fpath_list, key=lambda x: int(os.path.splitext(x)[0].split("_")[0]))

        collection_of_text = []

        for f_path in fpath_list_sorted:
            try:
                speech, rate = librosa.load(os.path.join(temp_dir_name, f_path), sr=16000)
                input_values = self.tokenizer(speech, return_tensors='pt', device=torch_device).input_values

                with torch.no_grad():
                    logits = self.model(input_values).logits

                predicted_ids = torch.argmax(logits, dim=-1)
                transcription = self.tokenizer.batch_decode(predicted_ids)[0]
                transcription = transcription.lower()
                #todo - remove print statement
                print(f"transcription: {transcription}")

                collection_of_text.append(transcription)
            except Exception as e:
                logging.error(f"> error in transcribing {f_path}")

        text = " ".join(collection_of_text)
        text_dict = {"output_text": text}

        # with open(os.path.join(output_dir_name, "output.json"), "w") as outfile:
        #     json.dump(text_dict, outfile)

        return text
