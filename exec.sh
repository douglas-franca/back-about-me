#!/bin/bash

# Install Python, pip, and venv
sudo apt install -y python3 python3-pip python3-venv

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required packages from requirements.txt
pip install -r requirements.txt

# Install gunicorn
pip install gunicorn

# Start the gunicorn server with 4 workers, binding to port 8000
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app