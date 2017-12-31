#!/usr/bin/python

import os
import sys
from subprocess import call

arg1 = sys.argv[1]

os.chdir('/CRM_2017')
os.system('npm install')
os.system('npm install forever')
if arg1 == "S1":
	os.system('export PORT=80; export DATABASE_URL=postgres://crm:xxxx@10.1.4.31:5432/crm; npm run-script migrate_local')
	os.system('export PORT=80; export DATABASE_URL=postgres://crm:xxxx@10.1.4.31:5432/crm; npm run-script seed_local')
os.system('export PORT=80; export DATABASE_URL=postgres://crm:xxxx@10.1.4.31:5432/crm; ./node_modules/forever/bin/forever start ./bin/www')

print('Servidor corriendo en '+arg1)