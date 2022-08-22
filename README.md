## Doc Archival Service
This repository performs audio transcription and text classification based on keywords to unstructured data i.e., text articles, audio files. 

### Input
Input to the program are text articles and audio files.
 

### Steps
**Step 1:** Clone this repository and install the dependencies.
```
$ pip install -r requirements.txt
```
**Step 2:** Download models required to perform audio transcription and text classification.
```
$ bash download_models.sh
```
**Step 3:** Change the working directory to /app. Run the FastAPI application.
```
$ uvicorn main:app --host="0.0.0.0" --port=80
```
 
 
 