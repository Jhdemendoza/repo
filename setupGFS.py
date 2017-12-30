#!/usr/bin/python

import os

os.system('sudo cp ./installGLUSTERFS.py /var/lib/lxc/nas1/rootfs/root')
os.system('sudo lxc-attach --clear-env -n nas1 -- python /root/installGLUSTERFS.py')