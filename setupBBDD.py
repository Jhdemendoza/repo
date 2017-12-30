#!/usr/bin/python

import os

os.system('sudo cp ./installBBDD.py /var/lib/lxc/bbdd/rootfs/root')
os.system('sudo lxc-attach --clear-env -n bbdd -- python /root/installBBDD.py')