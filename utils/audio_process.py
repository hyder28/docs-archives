from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.utils import make_chunks

import os
import logging


def load_audio_file(input_fpath, src_path):
    """load audio file"""
    try:
        logging.info(f"audio file path - {str(input_fpath)}")
        sound = None

        if input_fpath.endswith('.mp3') or input_fpath.endswith('.MP3'):
            sound = AudioSegment.from_mp3(input_fpath)
            sound.export(out_f=os.path.join(src_path, "mp3_file.wav"), format="wav")
        elif input_fpath.endswith('.wav') or input_fpath.endswith('.WAV'):
            sound = AudioSegment.from_wav(input_fpath)
            sound.export(out_f=os.path.join(src_path, "wav_file.wav"), format="wav")
        elif input_fpath.endswith('.ogg'):
            sound = AudioSegment.from_ogg(input_fpath)
            sound.export(out_f=os.path.join(src_path, "ogg_file.wav"), format="wav")
        elif input_fpath.endswith('.flac'):
            sound = AudioSegment.from_file(input_fpath, "flac")
            sound.export(out_f=os.path.join(src_path, "flac_file.wav"), format="wav")
        elif input_fpath.endswith('.3gp'):
            sound = AudioSegment.from_file(input_fpath, "3gp")
            sound.export(out_f=os.path.join(src_path, "3gp_file.wav"), format="wav")
        elif input_fpath.endswith('.3g'):
            sound = AudioSegment.from_file(input_fpath, "3gp")
            sound.export(out_f=os.path.join(src_path, "3gp.wav"), format="wav")

        sound.set_channels(1)
        sound.set_frame_rate(16000)
        duration = sound.duration_seconds

        logging.info(f"audio file duration - {str(duration)}s with frame rate - {str(sound.frame_rate)}")
    except Exception as e:
        logging.error(f"> error in loading file")


def create_audio_chunks(source_path, temp_path):
    """create audio chunks"""
    try:
        # create chunks
        audio_file_paths = os.listdir(source_path)
        if len(audio_file_paths) == 1:
            audio_filename = audio_file_paths[0]
        # todo - handle exceptions here correctly

        sound = AudioSegment.from_file(os.path.join(source_path, audio_filename))

        audio_chunks = []
        max_length = 30 * 1000

        for chunk in split_on_silence(sound, min_silence_len=500, silence_thresh=sound.dBFS - 14, keep_silence=500):
            if len(chunk) < max_length:
                audio_chunks.append(chunk)
            else:
                audio_chunks += make_chunks(chunk, max_length)

        for count, chunk in enumerate(audio_chunks):
            print(len(chunk) / 1000)
            output_fpath = os.path.join(temp_path, f"{count}_audio_file.wav")
            with open(output_fpath, "wb") as out_f:
                chunk.export(out_f, format="wav")
    except Exception as e:
        logging.error(f"> error in creating audio chunks")

