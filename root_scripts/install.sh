python -m venv .
source bin/activate
pip install --upgrade transformers
pip install --upgrade pip
pip install --upgrade sentencepiece
pip install --upgrade torch
pip install --upgrade accelerate
cp dot.profile ~/.profile
pip install --upgrade flask
ssh-keygen -t ed25519
