#!/usr/bin/python

import os
import sys
from setuptools import setup, find_packages

#either run as root or sudo
if os.getuid() !=0:
    print('Error: Need to run as root')
    sys.exit(1)

#install requirements if not installed already on the system
print('Ino: checking and installing requirements')
os.system('! dpkg -S python-imaging-tk && apt-get -y install python-imaging-tk')

#generate the requirements for old instructions
print('INFO: Generating the requirements from requirements.txt')
packages = []
for line in open('requirements.txt', 'r'):
    if not line.startswith('#'):
        packages.append(line.strip())

#run setup tools for pip
setup(
    name = 'FarquadsSmartMirror',
    version = '1.0.0',
    description = 'A Motion Detecting Smart Mirror powered by a Raspberry Pi3 which can display the Date, Time, Weather, A welcome Msg, a running Twitter feed, and Vidoes.',
    author = 'TheFarquadTeam',
    url = 'https://github.com/N03265566/Magic_Mirror',
    install_requires = packages,
    packages = find_packages(),
)