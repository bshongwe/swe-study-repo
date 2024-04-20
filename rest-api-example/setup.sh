#!/bin/bash

# Update package lists and installs Python and pip
# Take note that it will update dependencies installed
#        by requirements.txt
apt-get update
apt-get install -y python3 python3-pip

# Install required Python packages using pip
pip3 install -r requirements.txt

