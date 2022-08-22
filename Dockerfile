FROM nvidia/cuda:11.0-cudnn8-runtime-ubuntu18.04

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y curl
RUN apt-get install unzip
RUN apt-get -y install python3
RUN apt-get -y install python3-pip

WORKDIR /app

COPY requirements.txt requirements.txt
COPY /app .

RUN pip3 install -r requirements.txt

EXPOSE 80

# start the app
CMD ["uvicorn",  "main:app","--host=0.0.0.0","--port=80"]