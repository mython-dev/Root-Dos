#!/bin/bash

clear

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

if [[ "$OSTYPE" == "win32" ]]
    then echo "This script for only linux & Mac os"
    exit
fi

sudo apt update -y
sudo apt upgrade -y
pip3 install requests
pip3 install socket


chmod u+x attack.py

clear

echo "Successfully installed packages!"
echo "Please run: sudo python3 ./attack.py"