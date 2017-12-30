#!/usr/bin/python

import os

os.system('sudo cp ./setEnvCRM.py /var/lib/lxc/s1/rootfs/root')
os.system('sudo lxc-attach -n s1 -- python /root/setEnvCRM.py')

print('Variables de entorno configuradas en S1')

os.system('sudo cp ./setEnvCRM.py /var/lib/lxc/s2/rootfs/root')
os.system('sudo lxc-attach -n s2 -- python /root/setEnvCRM.py')

print('Variables de entorno configuradas en S2')

os.system('sudo cp ./setEnvCRM.py /var/lib/lxc/s3/rootfs/root')
os.system('sudo lxc-attach -n s3 -- python /root/setEnvCRM.py')

print('Variables de entorno configuradas en S3')

os.system('sudo cp ./installCRM.py /var/lib/lxc/s1/rootfs/root')
os.system('sudo lxc-attach -n s1 -- python /root/installCRM.py')

print('CRM instalado en S1')

os.system('sudo cp ./installCRM.py /var/lib/lxc/s2/rootfs/root')
os.system('sudo lxc-attach -n s2 -- python /root/installCRM.py')

print('CRM instalado en S2')

os.system('sudo cp ./installCRM.py /var/lib/lxc/s3/rootfs/root')
os.system('sudo lxc-attach -n s3 -- python /root/installCRM.py')

print('CRM instalado en S3')