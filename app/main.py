from fastapi import FastAPI, UploadFile
from typing import Union
from pydantic import BaseModel

import uvicorn
from app.utils import *

app = FastAPI()


class TextRequest(BaseModel):
    text: str


@app.get("/")
def root() -> dict:
    return {"message": "Lets process files!"}


@app.get("/health")
def check_health() -> dict:
    """
    Checks health
    """
    return {"status": "OK", "device": get_torch_device()}


@app.post("/process_text")
async def get_text_topic(text_request: TextRequest):
    """
    Extracts text
    """
    spacy_model = SpacySM()
    result = spacy_model.get_topic(text_request.text)

    return result

@app.post("/process_audio")
async def get_audio_topic(audio_file: Union[UploadFile, None] = None) -> dict:
    """
    Extracts audio
    """
    wav2vec2_model = Wav2Vec2()
    transcribed_text = wav2vec2_model.transcribe_text_from_file(audio_file.file, audio_file.filename)

    return transcribed_text

if __name__ == "__main__":
    uvicorn.run(app, port=5000)
