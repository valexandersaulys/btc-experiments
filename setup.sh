#!/bin/bash


git clone https://github.com/samr7/vanitygen
cd vanitygen
make

# at this point you can either symlink `keyconv` or run the python scripts within

sudo apt-get install python-qt4 python-pip
pip install requests
sudo pip install https://download.electrum.org/2.7.12/Electrum-2.7.12.tar.gz

