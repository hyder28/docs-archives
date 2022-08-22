# wav2vec2 models
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

model.save_pretrained('./app/models/wav2vec2-base-960h')
tokenizer.save_pretrained('./app/models/wav2vec2-base-960h')

# spacy models
#todo - add spacy model download here

"""
Steps:
1. fix broken packages: sudo apt -f install
2. update: sudo apt update && sudo apt dist-upgrade
3. install pip: sudo apt install python3-pip
4. check if pip installed: pip3 --version

5. pip install transformers: pip3 install transformers
6. pip install torch: pip3 install torch
7. download models: python3 download_models.py
"""