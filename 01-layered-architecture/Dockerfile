FROM ubuntu:22.04

COPY requirements.txt .

RUN apt-get update && apt-get upgrade
RUN apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]