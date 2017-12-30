#!env/usr/python 

import os 

os.system("apt-get update")
os.system("apt-get -y install postgresql")
print('CONFIGURANDO POSTGRES EN IP 10.1.4.31')
os.system('echo "listen_addresses = \'10.1.4.31\'" >> /etc/postgresql/9.6/main/postgresql.conf')
print('CONFIGURANDO "trust all"')
os.system('echo "host all all 10.1.4.0/24 trust" >> /etc/postgresql/9.6/main/pg_hba.conf')
print('CONFIGURANDO USUARIO crm CON PASSWORD xxxx')
os.system('echo "CREATE USER crm with PASSWORD \'xxxx\';" | sudo -u postgres psql')
print('CREANDO BASE DE DATOS crm')
os.system('echo "CREATE DATABASE crm;" | sudo -u postgres psql')
print('DAR TODOS LOS PRIVILEGIOS A USUARIO crm')
os.system('echo "GRANT ALL PRIVILEGES ON DATABASE crm to crm;" | sudo -u postgres psql')
os.system("systemctl restart postgresql")


