#!/bin/sh
useradd ai
mkdir /home/ai
chown ai:ai ~ai
usermod -s /bin/bash ai
cp -Rpp /notebooks/2025-05-10.1/* ~ai
cp -Rpp /notebooks/user/dot.profile /home/ai/.profile
chown ai:ai /home/ai/.profile
sudo -u ai -i ./0.sh
#sudo -u ai -i "uvicorn main:app --host 0.0.0.0 --port 5000"
#sudo -u ai bash -c "cd /home/ai && nohup uvicorn main:app --host 0.0.0.0 --port 5000"
