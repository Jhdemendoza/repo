#!/usr/bin/python

import os

os.system('apt-get update')
os.system('apt-get -y install curl')
os.system('curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -')
os.system('apt-get update')
os.system('apt-get install -y nodejs')

os.system('git clone https://github.com/CORE-UPM/CRM_2017.git')
os.chdir('/CRM_2017')
os.system('mkdir /CRM_2017/public/uploads')
os.system("mount -t glusterfs 10.1.4.21:/nas /CRM_2017/public/uploads")
os.system('node --version')
