#!/bin/bash

clear

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

cd .. 

sudo rm -r Root-Dos

clear

echo "Successfully uninstalled!"