#!/usr/bin/python

import os

os.system('sudo cp ./installFw.py /var/lib/lxc/fw/rootfs/root')
os.system('sudo lxc-attach --clear-env -n fw -- python /root/installFw.py')