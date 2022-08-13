from utils import clear_folder, load_audio_file, create_audio_chunks

from pathlib import Path
import logging

logging.basicConfig(filename="docs_archives_app.log", level=logging.DEBUG)

source_folder = Path("src/")
temp_folder = Path("tmp/")
output_folder = Path("output/")

clear_folder(source_folder)
clear_folder(temp_folder)
clear_folder(output_folder)

load_audio_file("data/audio/Paul Cobban - 5 mins.mp3", source_folder)
create_audio_chunks(source_folder, temp_folder)

