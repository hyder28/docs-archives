from utils import process_audio_file
import logging

import warnings

warnings.filterwarnings("ignore")

logging.basicConfig(filename="app.log", level=logging.DEBUG)

# transcribe audio into text
input_fpath = "data/audio/Paul Cobban - 5 mins.mp3"
text = process_audio_file(input_fpath)
