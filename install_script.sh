#!/bin/bash
#run this as bash script with elevated permission
sudo apt install python3-venv

python3 -m venv venv

. venv/bin/activate
python3 -m pip --version
python3 -m pip install --user --upgrade pip
python3 -m pip install --upgrade pip

which python

python3 -m pip install selenium
python3 -m pip install pandas
#copy this line above and change the last word for each new Lib to install

#export dependencies to a file for future use
python3 -m pip freeze > requeriments.txt