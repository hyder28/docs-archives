# wav2vec2 models
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

model.save_pretrained('./models/wav2vec2-base-960h-v2')
tokenizer.save_pretrained('./models/wav2vec2-base-960h-v2')

# spacy models