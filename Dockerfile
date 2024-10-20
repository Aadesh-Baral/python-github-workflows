FROM ubuntu:latest as base

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN python3 -m venv my-venv

SHELL ["/bin/bash", "-c"]
RUN source my-venv/bin/activate && \
    pip3 install --upgrade pip && \
    pip3 install -r ./requirements.txt

COPY requirements.txt ./requirements.txt
