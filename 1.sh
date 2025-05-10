#!/bin/bash
pip install --upgrade pip
pip install --upgrade torch transformers accelerate sentencepiece
cp dot.profile ~/.profile
pip install --upgrade flask
ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519
