#!/usr/bin/python

import os
from subprocess import call

os.system('sudo cp ./startServer.py /var/lib/lxc/s1/rootfs/root')
call(['sudo', 'lxc-attach', '-n', 's1', '--', 'python', '/root/startServer.py', 'S1'])

os.system('sudo cp ./startServer.py /var/lib/lxc/s2/rootfs/root')
call(['sudo', 'lxc-attach', '-n', 's2', '--', 'python', '/root/startServer.py', 'S2'])

os.system('sudo cp ./startServer.py /var/lib/lxc/s3/rootfs/root')
call(['sudo', 'lxc-attach', '-n', 's3', '--', 'python', '/root/startServer.py', 'S3'])