#!/bin/bash
echo "verify libraries..."
python -c '
import librosa;
import torch;
import pydub;
'
echo "verify models..."
python -c '
import spacy;
spacy.load("./models/en_core_web_sm-3.4.0");
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer;
model = Wav2Vec2ForCTC.from_pretrained("models/wav2vec2-large-960h",local_files_only=True)
'