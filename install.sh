#!/usr/bin/env bash

sudo apt-get install python3-pip -y
pip3 install bs4
PATH="/usr/local/bin"
/usr/bin/sudo rm -rf $PATH/name-gen $PATH/name-generator
/usr/bin/sudo /usr/bin/cp -a $PWD $PATH/name-generator
/usr/bin/sudo cp -a $PWD/name-gen $PATH/name-gen
./get-names.py
