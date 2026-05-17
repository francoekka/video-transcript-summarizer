#!/bin/bash

# Install necessary packages
pip install youtube-transcript-api==1.2.4 \
            faiss-cpu==1.8.0 \
            langchain==0.2.6 \
            langchain-community==0.2.6 \
            gradio==4.44.1 \
            sentence-transformers==1.14.0

# Uninstall any existing huggingface_hub first
python3.11 -m pip uninstall -y huggingface_hub

# Install a version compatible with gradio 4.44.1
python3.11 -m pip install huggingface_hub==0.16.4

# Upgrade supporting packages
pip install --upgrade gradio fastapi starlette jinja2

pip install -U langchain-huggingface
