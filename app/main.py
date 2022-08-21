from fastapi import FastAPI
import uvicorn

from app.utils import get_torch_device

app = FastAPI()

@app.get("/")
def root() -> dict:
    return {"message": "Lets process files!"}

@app.get("/health")
def check_health() -> dict:
    """
    Checks health
    """
    torch_device = get_torch_device()

    return {"status": "OK", "Device": torch_device}


if __name__ == "__main__":
    uvicorn.run(app, port=5000)
