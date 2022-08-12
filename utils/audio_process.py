from pydub import AudioSegment
from pydub.utils import make_chunks

import os
import logging


def load_audio_file(source_path, target_path):
    """load audio file"""
    try:
        sound = None
        if source_path.endswith('.mp3') or source_path.endswith('.MP3'):
            sound = AudioSegment.from_mp3(source_path)
        elif source_path.endswith('.wav') or source_path.endswith('.WAV'):
            sound = AudioSegment.from_wav(source_path)
        elif source_path.endswith('.ogg'):
            sound = AudioSegment.from_ogg(source_path)
        elif source_path.endswith('.flac'):
            sound = AudioSegment.from_file(source_path, "flac")
        elif source_path.endswith('.3gp'):
            sound = AudioSegment.from_file(source_path, "3gp")
        elif source_path.endswith('.3g'):
            sound = AudioSegment.from_file(source_path, "3gp")

        sound.export(target_path, "wav")
        duration = sound.duration_seconds

        return sound, duration
    except Exception as e:
        logging.error(f"> error in loading file")

        return None, None


def create_audio_chunks(source_path, temp_path, chunk_length=30):
    """create audio chunks"""
    try:
        # create chunks
        sound = AudioSegment.from_file(source_path)
        audio_chunks = make_chunks(sound, chunk_length * 1000)

        for count, chunk in enumerate(audio_chunks):
            output_fpath = os.path.join(temp_path, f"{count}_audio_file.wav")
            with open(output_fpath, "wb") as out_f:
                chunk.export(out_f, format="wav")
    except Exception as e:
        logging.error(f"> error in creating audio chunks")


