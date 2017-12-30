#!/usr/bin/python

import os
import sys

arg1 = sys.argv[1]

os.chdir('/CRM_2017')
os.system('npm install forever')
if arg1 == "S1":
	os.system('npm run-script migrate_local')
	os.system('npm run-script seed_local')
os.system('./node_modules/forever/bin/forever start ./bin/www')

print('Servidor corriendo en '+arg1)