from app.utils import Wav2Vec2, SpacySM
import os
import json
import logging
import warnings

#todo: expose as an api
#todo: create python script to download pre-trained models
print(os.getcwd())
warnings.filterwarnings("ignore")
logging.basicConfig(filename="app.log", level=logging.INFO)

# input file directories
input_audio_dir = "/Users/hyderali/Documents/data/docs-archives/audio"
input_text_dir = "/Users/hyderali/Documents/data/docs-archives/text/test_texts.txt"

# initialize models
wav2vec2_model = Wav2Vec2()
spacy_model = SpacySM()

"""
1. wav2vec2 model - transcribe audio
"""
result_audio = dict()
for file in os.listdir(input_audio_dir):
    input_fpath = os.path.join(input_audio_dir, file)

    transcribed_text = wav2vec2_model.transcribe_text(input_fpath)
    result_audio[str(file)] = transcribed_text

print(json.dumps(result_audio, indent = 4))

"""
2. spacy model usage - identify text topics
"""
with open(input_text_dir) as file:
    text_list = [line for line in file if line.strip()]

for text in text_list:
    text_topic = spacy_model.get_topic(text)
    print(text_topic)
