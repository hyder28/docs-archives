from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn

from app.utils import get_torch_device, SpacySM

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


@app.post("/text_topic")
def get_topics(user_request_in: TextRequest):
    spacy_model = SpacySM()
    result = spacy_model.get_topic(user_request_in.text)

    return result


if __name__ == "__main__":
    uvicorn.run(app, port=5000)
