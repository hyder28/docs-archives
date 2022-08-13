from utils import process_audio_file
import os
import json
import logging
import warnings

warnings.filterwarnings("ignore")
logging.basicConfig(filename="app.log", level=logging.DEBUG)

# transcribe audio into text
input_data_dir = "data/audio"

result = dict()

for file in os.listdir(input_data_dir):
    input_fpath = os.path.join(input_data_dir, file)
    text = process_audio_file(input_fpath)
    result[str(file)] = text

print(json.dumps(result, indent = 4))