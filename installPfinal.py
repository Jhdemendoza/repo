#!/usr/bin/python

import os

os.system('/home/cdps/pfinal/bin/prepare-pfinal-vm')
os.system('vnx -f /home/cdps/pfinal/pfinal.xml --create')

print('Configurando firewall...')
os.system('python ./setupFw.py')
print('Firewall configurado!!')

print('Configurando Base de Datos...')
os.system('python ./setupBBDD.py')
print('Base de datos configurada!!')

print('Configurando cluster de almacenamiento...')
os.system('python ./setupGFS.py')
print('Cluster de almacenamiento configurado!!')

print('Configurando CRM...')
os.system('python ./setupServerCRM.py')
print('CRM configurado!!')

print('Arrancando CRM...')
os.system('python ./startCRM.py')
print('CRM corriendo!!')

print('Configurando balanceador de carga...')
os.system('python ./setupLb.py')
print('Balanceador de carga configurado!!')


