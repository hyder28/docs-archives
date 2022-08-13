from utils import Wav2Vec2
import os
import json
import logging
import warnings

warnings.filterwarnings("ignore")
logging.basicConfig(filename="app.log", level=logging.INFO)

# transcribe audio into text
input_data_dir = "data/audio"

result = dict()

for file in os.listdir(input_data_dir):
    input_fpath = os.path.join(input_data_dir, file)

    # wav2vec asr
    wav2vec2_model = Wav2Vec2()
    transcribed_text = wav2vec2_model.transcribe_text(input_fpath)

    result[str(file)] = transcribed_text

print(json.dumps(result, indent = 4))