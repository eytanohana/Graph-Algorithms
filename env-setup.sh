#!/bin/bash

# requires python 3.11 to be installed
echo "creating python3.11 env in .venv directory"
python3.11 -m venv .venv
source .venv/bin/activate
echo "Installing requirements..."
pip install -r requirements.txt
