from app.utils import Wav2Vec2, SpacySM
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
print(os.getcwd())
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
text = """A joint session of Italian parliament and some regional delegates, \
known as “great electors,” began a secret ballot on Monday to elect the next \
Italian president to replace the current officeholder, Sergio Mattarella. \
It is a focus of special attention because a top contender for the job is \
the prime minister, Mario Draghi, a titan of Europe who in just a year in \
power has stabilized Italy’s politics and initiated long-overdue overhauls."""
text_topic = spacy_model.get_topic(text)
print(text_topic)
