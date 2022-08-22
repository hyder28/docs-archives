# wav2vec2 models
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

model.save_pretrained('./app/models/wav2vec2-base-960h')
tokenizer.save_pretrained('./app/models/wav2vec2-base-960h')

# spacy models
#todo - add spacy model download here