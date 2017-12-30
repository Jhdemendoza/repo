#!/usr/bin/python

import os

os.system('sudo lxc-attach -n lb -- xr --server tcp:0:80 --backend 10.1.3.11:80 --backend 10.1.3.12:80 --backend 10.1.3.13:80 --web-interface 0:8001 -dr &')
print('Balanceador de carga funcionando')