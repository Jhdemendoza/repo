#!/usr/bin/python

import os
import sys
from subprocess import call

def create():
	os.system('cp /home/cdps/pfinal/pfinal.xml ./pfinal_backup.xml')
	if arg2 == 3:
		os.system('/home/cdps/pfinal/bin/prepare-pfinal-vm')
		os.system('vnx -f /home/cdps/pfinal/pfinal.xml --create')
		fileServ = open('./nServ.txt', 'w')
		fileServ.write("3")
		fileServ.close()
	else:
		for i in range(arg2-3):
			j = i+1
			index = str(j+3)
			indexAux = str(j+2)
			print("i: ", i, "j: ", j, "index: ", index, "index_aux: ", indexAux)
			fileWrite = open('./pfinal_aux.xml', 'w')
			fileRead = open('/home/cdps/pfinal/pfinal.xml', 'r')
			for line in fileRead:
				if '<ipv4>10.1.4.1'+indexAux+'/24</ipv4>' in line:
					fileWrite.write(line)
					fileWrite.write('</if>\n<if id="9" net="virbr0">\n<ipv4>dhcp</ipv4>\n</if>\n<route type="ipv4" gw="10.1.3.1">10.1.0.0/16</route>\n<exec seq="on_boot" type="verbatim">\nmknod -m 666 /dev/fuse c 10 229;\n</exec>\n</vm>\n\n<vm name="s'+str(index)+'" type="lxc" arch="x86_64">\n<filesystem type="cow">filesystems/rootfs_lxc64-cdps</filesystem>\n<if id="1" net="LAN3">\n<ipv4>10.1.3.1'+index+'/24</ipv4>\n</if>\n<if id="2" net="LAN4">\n<ipv4>10.1.4.1'+index+'/24</ipv4>\n')
				else:
					fileWrite.write(line)
			fileRead.close()
			fileWrite.close()
			os.system('cp ./pfinal_aux.xml /home/cdps/pfinal/pfinal.xml')
			os.system('rm ./pfinal_aux.xml -f')
		fileServ = open('./nServ.txt', 'w')
		fileServ.write(str(arg2))
		fileServ.close()
		os.system('/home/cdps/pfinal/bin/prepare-pfinal-vm')
		os.system('vnx -f /home/cdps/pfinal/pfinal.xml --create')


def firewall():
	print('Configurando firewall...')
	os.system('sudo cp ./installFw.py /var/lib/lxc/fw/rootfs/root')
	os.system('sudo lxc-attach --clear-env -n fw -- python /root/installFw.py')
	print('Firewall configurado!!')

def bbdd():
	print('Configurando Base de Datos...')
	os.system('sudo cp ./installBBDD.py /var/lib/lxc/bbdd/rootfs/root')
	os.system('sudo lxc-attach --clear-env -n bbdd -- python /root/installBBDD.py')
	print('Base de datos configurada!!')

def cluster():
	print('Configurando cluster de almacenamiento...')
	os.system('sudo cp ./installGLUSTERFS.py /var/lib/lxc/nas1/rootfs/root')
	os.system('sudo lxc-attach --clear-env -n nas1 -- python /root/installGLUSTERFS.py')
	print('Cluster de almacenamiento configurado!!')

def setCRM():
	print('Configurando pariables de entorno del CRM...')
	numServ = 0
	fileServ = open('./nServ.txt', 'r')
	for line in fileServ:
		numServ = int(line)

	for i in range(numServ):
		j = i+1
		os.system('sudo cp ./setEnvCRM.py /var/lib/lxc/s'+str(j)+'/rootfs/root')
		os.system('sudo lxc-attach -n s'+str(j)+' -- python /root/setEnvCRM.py')
		print('Variables de entorno configuradas en S'+str(j)+'\n')
	
		os.system('sudo cp ./installCRM.py /var/lib/lxc/s'+str(j)+'/rootfs/root')
		os.system('sudo lxc-attach -n s'+str(j)+' -- python /root/installCRM.py')
		print('CRM instalado en S'+str(j)+'\n')
	
	print('CRM configurado!!')

def runCRM():
	print('Arrancando CRM...')
	numServ = 0
	fileServ = open('./nServ.txt', 'r')
	for line in fileServ:
		numServ = int(line)

	for i in range(numServ):
		j = i+1
		os.system('sudo cp ./startServer.py /var/lib/lxc/s'+str(j)+'/rootfs/root')
		call(['sudo', 'lxc-attach', '-n', 's'+str(j)+'', '--', 'python', '/root/startServer.py', 'S'+str(j)+''])
	print('CRM corriendo!!')

def lb():
	print('Configurando balanceador de carga...')
	numServ = 0
	fileServ = open('./nServ.txt', 'r')
	for line in fileServ:
		numServ = int(line)

	balan = 'sudo lxc-attach -n lb -- xr --server tcp:0:80 '
	for i in range(numServ):
		j = i+1
		balan += '--backend 10.1.3.1'+str(j)+':80 '

	balan += '--web-interface 0:8001 -dr &'

	os.system(balan)
	print('Balanceador de carga configurado y funcionando!!\n\n')
        print('Abra un nuevo terminal si necesita conectarse a alguna de las máquinas o si quiere destruir el escenario\n')

def help():
        print('Configurar y arrancar todo: sudo python installPfinal.py doItAll\n')
        print('Configurar un número de servidores mayor que 3: sudo python installPfinal.py create [nServ]\n')
        print('Terminar de configurar y arrancar el escenario: sudo python installPfinal.py doTheRest\n')
	print('Configurar escenario (MVs): sudo python installPfinal.py create\n')
	print('Configurar firewall: sudo python installPfinal.py firewall\n')
	print('Configurar base de datos: sudo python installPfinal.py bbdd\n')
	print('Configurar cluster de almacenamiento: sudo python installPfinal.py cluster\n')
	print('Configurar CRM: sudo python installPfinal.py setCRM\n')
	print('Arrancar el servicio CRM: sudo python installPfinal.py runCRM\n')
	print('Configurar y arrancar el balanceador de carga: sudo python installPfinal.py lb\n')

def destroy():
	os.system('rm ./nServ.txt -f')
	os.system('sudo vnx -f /home/cdps/pfinal/pfinal.xml --destroy')
	os.system('cp ./pfinal_backup.xml /home/cdps/pfinal/pfinal.xml')


if (len(sys.argv) > 1):
	arg1 = sys.argv[1]
	arg2 = int("3")
else:
	arg1 = "help"

if arg1 == "create":
	if (len(sys.argv) > 2):
		arg2 = int(sys.argv[2])
	create()
elif arg1 == "firewall":
	firewall()
elif arg1 == "bbdd":
	bbdd()
elif arg1 == "cluster":
	cluster()
elif arg1 == "setCRM":
	setCRM()
elif arg1 == "runCRM":
	runCRM()
elif arg1 == "lb":
	lb()
elif arg1 == "doItAll":
	create()
	firewall()
	bbdd()
	cluster()
	setCRM()
	runCRM()
	lb()
elif arg1 == "doTheRest":
	firewall()
	bbdd()
	cluster()
	setCRM()
	runCRM()
	lb()
elif arg1 == "destroy":
	destroy()
else:
	help()


