#!env/usr/python 

import os

#anadimos los servidores
os.system("gluster peer probe 10.1.4.22")
os.system("gluster peer probe 10.1.4.23")

#configuramos los servidores para que se replique la informacion entre ellos 
os.system("gluster volume create nas replica 3 10.1.4.21:/nas 10.1.4.22:/nas 10.1.4.23:/nas force")
os.system("gluster volume start nas")
#cambiamos el timeout de los servidores 
os.system("gluster volume set nas network.ping-timeout 5")

