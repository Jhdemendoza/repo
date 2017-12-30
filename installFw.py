#!/usr/bin/python

import os

os.system('git clone https://github.com/Jhdemendoza/firewall.git')
os.chdir('./firewall')
os.system('sudo ./fw.fw start')