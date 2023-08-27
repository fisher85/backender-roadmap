FROM alpine:3.8
COPY requirements.txt .
RUN apk add --no-cache python3 alpine-sdk python3-dev libffi-dev openssl-dev && \
    pip3 install -r requirements.txt

WORKDIR /app

