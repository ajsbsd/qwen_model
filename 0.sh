#!/bin/bash
python -m venv .
source /home/ai/bin/activate
pip install --upgrade pip
pip install --upgrade torch transformers accelerate sentencepiece
cp /home/ai/dot.profile /home/ai/.profile
pip install --upgrade flask
ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519
mkdir -p ~/qwen_model
cd ~/qwen_model
git lfs install
git clone https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct  .
git config --global credential.helper store
pip install fastapi uvicorn
