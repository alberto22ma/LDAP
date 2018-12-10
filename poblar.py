#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ldap
from ldap import modlist
import getpass
import csv

# Values #
conection = "ldap://172.22.200.118:389/"
file_name = 'usuarios.csv'
dom = 'dc=rajoy,dc=albertomoreno,dc=gonzalonazareno,dc=org'
uidNumberInitial = 2000
gidNumber = 2002


user = 'admin'
passwd = getpass.getpass('Contraseña del usuario %s LDAP: ' % user)

with open('usuarios.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)

try:
	bind = "cn=%s,%s" % (user, dom)
	l = ldap.initialize(conection)
	l.simple_bind_s(bind,passwd)

	for i in reader['usuarios']:
		nombre = i['nombre'].encode('utf8')
		apellidos = i['apellidos'].encode('utf8')
		uid = str(i['usuario'])
		attrs = {}
		dn="uid=%s,ou=People,dc=rajoy,dc=albertomoreno,dc=gonzalonazareno,dc=org" % str(i["usuario"])
		attrs['objectClass'] = ['top', 'posixAccount', 'inetOrgPerson', 'ldapPublicKey']
		attrs['uid'] = uid
		attrs['cn'] = nombre
		attrs['sn'] = apellidos
		attrs['mail'] = str(i['correo'])
		attrs['uidNumber'] = str(uidNumberInitial)
		attrs['gidNumber'] = str(gidNumber)
		attrs['homeDirectory'] = '/home/%s' % uid
		attrs['loginShell'] = '/bin/bash'
		attrs['sshPublicKey'] = str(i['clave'])
		ldif = modlist.addModlist(attrs)
		try:
			l.add_s(dn,ldif)
			uidNumber = uidNumber + 1
			print 'Usuario %s insertado.' % uid 
		except:
			print "El usuario %s ya existe." % str(i["usuario"])
	for i in reader["equipos"]:
		dn="uid=%s,ou=Computers,dc=rajoy,dc=albertomoreno,dc=gonzalonazareno,dc=org" % str(i["ipv4"])
		attrs1 = {}
		attrs1['objectclass'] = ['top','device','ldapPublicKey','ipHost']
		attrs1['cn'] = str(i["hostname"])
		attrs1['ipHostNumber'] = str(i["ipv4"])
		attrs1['sshPublicKey'] = str(i["clave"])
		ldif = modlist.addModlist(attrs1)
		l.add_s(dn,ldif)
		print 'Computer %s insertado.' % str(i["ipv4"])
	l.unbind_s()
except ldap.LDAPError, e:
	print 'ERROR: ' + e[0]['desc']

