#!/bin/bash

if [ ! -d directory ]; then
  python3 -m venv env
fi
source env/bin/activate
python3 -m pip install -r requirements.txt