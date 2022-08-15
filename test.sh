#!/bin/bash
echo "verify libraries"
python -c '
import transformers;
import librosa;
import torch;
import spacy;
import pydub;
'