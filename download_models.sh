 python -c '
from transformers import Wav2Vec2ForCTC;
from transformers import Wav2Vec2Tokenizer;

tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h");
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h");

model.save_pretrained("./app/models/wav2vec2-base-960h-new");
tokenizer.save_pretrained("./app/models/wav2vec2-base-960h-new");
 '
python -m spacy download en_core_web_sm
python -c '
import spacy;

nlp = spacy.load("en_core_web_sm");
nlp.to_disk("./app/models/en_core_web_sm-new");
'