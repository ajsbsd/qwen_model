#!/bin/bash
mkdir -p ~/qwen_model
cd ~/qwen_model
git lfs install
git clone https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct  .
git config --global credential.helper store
