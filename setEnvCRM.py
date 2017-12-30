#!/usr/bin/python

import os

file = open('/etc/environment', 'a')
file.write('DATABASE_URL=postgres://crm:xxxx@10.1.4.31:5432/crm\n')
file.close()
file = open('/etc/environment', 'a')
file.write('PORT=80\n')
file.close()