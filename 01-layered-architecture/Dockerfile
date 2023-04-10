FROM ubuntu:22.04

RUN apt-get update && apt-get upgrade
RUN apt-get install -y python3 python3-pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /app

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]