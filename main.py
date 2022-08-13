from utils import clear_folder, load_audio_file, create_audio_chunks
from utils import dir_list, source_dir_name, temp_dir_name, output_dir_name

from pathlib import Path
import logging

logging.basicConfig(filename="app.log", level=logging.DEBUG)

for dir in dir_list:
    clear_folder(dir)

load_audio_file("data/audio/Piyush2 - 5 mins.mp3", source_dir_name)
create_audio_chunks(source_dir_name, temp_dir_name)

