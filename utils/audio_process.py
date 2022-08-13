import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
from .constants import wav2vec2_model_dir

from pydub import AudioSegment
from pydub.utils import make_chunks
from pydub.silence import split_on_silence

import os
import json
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

        sound.set_frame_rate(16000)
        duration = sound.duration_seconds

        logging.info(f"audio file duration - {str(duration)}s with frame rate - {str(sound.frame_rate)}")
    except Exception as e:
        logging.error(f"> error in loading file")


def create_audio_chunks(source_path, temp_path, chunk_length=30):
    """create audio chunks"""
    try:
        # create chunks
        audio_file_paths = os.listdir(source_path)
        if len(audio_file_paths) == 1:
            audio_filename = audio_file_paths[0]

        sound = AudioSegment.from_file(os.path.join(source_path, audio_filename))
        # audio_chunks = make_chunks(sound, chunk_length * 1000)
        audio_chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=sound.dBFS - 14, keep_silence=500)

        for count, chunk in enumerate(audio_chunks):
            output_fpath = os.path.join(temp_path, f"{count}_audio_file.wav")
            with open(output_fpath, "wb") as out_f:
                chunk.export(out_f, format="wav")
    except Exception as e:
        logging.error(f"> error in creating audio chunks")


def get_audio_transcription(temp_path, target_path):
    """get audio transcriptions"""
    try:
        tokenizer = Wav2Vec2Tokenizer.from_pretrained(wav2vec2_model_dir, local_files_only=True)
        model = Wav2Vec2ForCTC.from_pretrained(wav2vec2_model_dir, local_files_only=True)

        collection_of_text = []

        fpath_list = os.listdir(temp_path)
        fpath_list_sorted = sorted(fpath_list, key=lambda x: int(os.path.splitext(x)[0].split("_")[0]))

        for f_path in fpath_list_sorted:
            speech, rate = librosa.load(os.path.join(temp_path, f_path), sr=16000)
            input_values = tokenizer(speech, return_tensors='pt').input_values

            with torch.no_grad():
                logits = model(input_values).logits

            predicted_ids = torch.argmax(logits, dim=-1)
            transcription = tokenizer.batch_decode(predicted_ids)[0]
            transcription = transcription.lower()
            collection_of_text.append(transcription)

        text = " ".join(collection_of_text)
        text_dict = {"output_text": text}

        with open(os.path.join(target_path, "output.json"), "w") as outfile:
            json.dump(text_dict, outfile)

        return text

    except Exception as e:
        logging.error(f"> error in transcribing audio chunks")
        return ""
