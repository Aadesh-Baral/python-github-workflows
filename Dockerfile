FROM ubuntu:latest as base

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN python3 -m venv my-venv

RUN . my-venv/bin/activate

RUN pip3 install --upgrade pip

COPY requirements.txt ./requirements.txt

RUN pip3 install -r ./requirements.txt
