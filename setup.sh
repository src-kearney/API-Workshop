#!/bin/bash
echo "Creating Python3 Virtual Environment"
virtualenv -p python3 venv
echo "Activating Virtual Environment"
source "./venv/bin/activate"
echo "Installing required packages"
pip install -r requirements.txt
