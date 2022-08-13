from .audio_process import *
from .file_process import *
from .constants import *


def process_audio_file(input_fpath):
    """transcribe text from an input fpath"""
    process_clean_all_folders()
    load_audio_file(input_fpath, source_dir_name)
    create_audio_chunks(source_dir_name, temp_dir_name)

    text = get_audio_transcription(temp_dir_name, output_dir_name)

    return text
