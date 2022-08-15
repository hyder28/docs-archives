from utils import Wav2Vec2, SpacySM
import os
import json
import logging
import warnings

warnings.filterwarnings("ignore")
logging.basicConfig(filename="app.log", level=logging.INFO)

"""
Packages:
spacy, transformers, librosa
"""

"""
1. wav2vec2 model - transcribe audio
"""
input_data_dir = "data/audio"
result_audio = dict()
for file in os.listdir(input_data_dir):
    input_fpath = os.path.join(input_data_dir, file)

    wav2vec2_model = Wav2Vec2()
    transcribed_text = wav2vec2_model.transcribe_text(input_fpath)
    result_audio[str(file)] = transcribed_text

print(json.dumps(result_audio, indent = 4))

"""
2. spacy model usage - identify text topics
"""
spacy_model = SpacySM()
text = "Hello, my name is Hyder Ali. I was born in Singapore and have been living at Eunos for the past 30 years."
text_topic = spacy_model.get_topic(text)
print(text_topic)
