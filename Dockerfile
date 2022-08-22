FROM nvidia/cuda:11.0-cudnn8-runtime-ubuntu18.04

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y curl
RUN apt-get install unzip
RUN apt-get -y install python3
RUN apt-get -y install python3-pip

WORKDIR /app

COPY requirements.text requirements.txt
COPY /app .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "-m" , "main", "--host=0.0.0.0"]