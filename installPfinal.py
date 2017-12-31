#!/usr/bin/python

import os
import sys

if (len(sys.argv) > 1):
	arg1 = sys.argv[1]
else:
	arg1 = "help"
if arg1 == "create":
	os.system('/home/cdps/pfinal/bin/prepare-pfinal-vm')
	os.system('vnx -f /home/cdps/pfinal/pfinal.xml --create')
elif arg1 == "firewall":
	print('Configurando firewall...')
	os.system('python ./setupFw.py')
	print('Firewall configurado!!')
elif arg1 == "bbdd":
	print('Configurando Base de Datos...')
	os.system('python ./setupBBDD.py')
	print('Base de datos configurada!!')
elif arg1 == "cluster":
	print('Configurando cluster de almacenamiento...')
	os.system('python ./setupGFS.py')
	print('Cluster de almacenamiento configurado!!')
elif arg1 == "setCRM":
	print('Configurando pariables de entorno del CRM...')
	os.system('python ./setEnv.py')
	print('Variables de entorno configuradas en CRMs')
	print('Configurando CRM...')
	os.system('python ./setupServerCRM.py')
	print('CRM configurado!!')
elif arg1 == "runCRM":
	print('Arrancando CRM...')
	os.system('python ./startCRM.py')
	print('CRM corriendo!!')
elif arg1 == "lb":
	print('Configurando balanceador de carga...')
	os.system('python ./setupLb.py')
	print('Balanceador de carga configurado!!')
else:
	print('Configurar escenario (MVs): sudo python installPfinal.py create\n')
	print('Configurar firewall: sudo python installPfinal.py firewall\n')
	print('Configurar base de datos: sudo python installPfinal.py bbdd\n')
	print('Configurar cluster de almacenamiento: sudo python installPfinal.py cluster\n')
	print('Configurar CRM: sudo python installPfinal.py setCRM\n')
	print('Arrancar el servicio CRM: sudo python installPfinal.py runCRM\n')
	print('Configurar y arrancar el balanceador de carga: sudo python installPfinal.py lb\n')

