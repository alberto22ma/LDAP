#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ldap
import csv
import ldap.modlist as modlist
import getpass

#Abrir fichero
alumnos = open("usuarios.csv")
datosalumnos = csv.load(alumnos)

servidor='ldap://rajoy.albertomoreno.gonzalonazareno.org:389'
conection = "ldap://172.22.200.118:389/"
file_name = 'usuarios.csv'
dom = 'dc=albertomoreno,dc=gonzalonazareno,dc=org'
uidNumberInitial = 2000
gidNumber = 2005

#Solicitamos la identificacion para el administrador de ldap
password = getpass.getpass("Identificacion administrador LDAP: ")

for i in datos["usuarios"]:
        dn="uid=%s,ou=People,dc=albertomoreno,dc=gonzalonazareno,dc=org" % str(i["usuario"])
        attrs = {}
        attrs['objectclass'] = ['top','posixAccount','inetOrgPerson','ldapPublicKey']
        attrs['cn'] = str(i["nombre"])
        attrs['uid'] = str(i["usuario"])
        attrs['sn'] = str(i["apellidos"])
        attrs['uidNumber'] = str(uidNumber)
        attrs['gidNUmber'] = str(gidNumber)
        attrs['mail'] = str(i["correo"])
        attrs['sshPublicKey'] = "ssh-rsa" + str(i["clave"])
        attrs['homeDirectory'] = ['/home/%s' % (str(i["usuario"]))]
        attrs['loginShell'] = ['/bin/bash']
        ldif = modlist.addModlist(attrs)
        uri.add_s(dn,ldif)
        uidNumber = uidNumber + 1

uri.unbind_s()
alumnos.close()


