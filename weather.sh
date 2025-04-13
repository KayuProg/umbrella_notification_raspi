#!/bin/bash
export HOME=/home/kayu
export TERM=xterm
cd /home/kayu/Desktop/umbrella_notification_raspi/
source .venv/bin/activate
PYTHON_SCRIPT="/home/kayu/Desktop/umbrella_notification_raspi/main.py"
python3 $PYTHON_SCRIPT> /home/kayu/Desktop/output.log 2>&1