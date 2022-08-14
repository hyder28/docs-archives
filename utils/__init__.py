from .audio_process import *
from .file_process import *
from .constants import *

from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import librosa
import torch
import spacy
from spacy.matcher import Matcher
import collections
import json


class SpacySM:
    """spacy en-core-web-sm-3.4.0"""

    def __init__(self):
        self.nlp = spacy.load(spacy_model_dir)
        self.matcher = Matcher(self.nlp.vocab)

    def get_topic(self, text):
        try:
            text = text.lower()

            for keyword_class, keyword_list in keywords_dict.items():
                for key_word in keyword_list:
                    pattern = [{"LOWER": key_word}]
                    self.matcher.add(keyword_class, [pattern])

            doc = self.nlp(text)
            matches = self.matcher(doc)

            result_list = []
            for match_id, start, end in matches:
                rule_id = self.nlp.vocab.strings[match_id]
                span = doc[start:end]

                result_list.append((rule_id, span.text))

            ctr = collections.Counter(result_list)

            return ctr
        except Exception as e:
            logging.error(f"> error in text topic extraction")
            return {}

class Wav2Vec2:
    """wav2vec2 for asr"""

    def __init__(self):
        self.tokenizer = Wav2Vec2Tokenizer.from_pretrained(wav2vec2_model_dir, local_files_only=True)
        self.model = Wav2Vec2ForCTC.from_pretrained(wav2vec2_model_dir, local_files_only=True)

    def transcribe_text(self, input_fpath):
        process_clean_all_folders()

        # audio files processing
        load_audio_file(input_fpath, source_dir_name)
        create_audio_chunks(source_dir_name, temp_dir_name)

        fpath_list = os.listdir(temp_dir_name)
        fpath_list_sorted = sorted(fpath_list, key=lambda x: int(os.path.splitext(x)[0].split("_")[0]))

        collection_of_text = []

        for f_path in fpath_list_sorted:
            try:
                speech, rate = librosa.load(os.path.join(temp_dir_name, f_path), sr=16000)
                input_values = self.tokenizer(speech, return_tensors='pt').input_values

                with torch.no_grad():
                    logits = self.model(input_values).logits

                predicted_ids = torch.argmax(logits, dim=-1)
                transcription = self.tokenizer.batch_decode(predicted_ids)[0]
                transcription = transcription.lower()
                collection_of_text.append(transcription)
            except Exception as e:
                logging.error(f"> error in transcribing {f_path}")

        text = " ".join(collection_of_text)
        text_dict = {"output_text": text}

        with open(os.path.join(output_dir_name, "output.json"), "w") as outfile:
            json.dump(text_dict, outfile)

        return text
