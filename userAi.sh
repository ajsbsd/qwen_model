#!/bin/sh
useradd ai
mkdir /home/ai
chown ai:ai ~ai
usermod -s /bin/bash ai
cp -Rpp /notebooks/2025-05-10/* ~ai
cp -Rpp /notebooks/user/dot.profile /home/ai/.profile
chown ai:ai /home/ai/.profile
