#!/bin/bash
key=$(ldapsearch -x -h localhost '(&(objectClass=posixAccount)(uid='"$1"'))' 'sshPublicKey' | sed -n '/^ /{H;d};/sshPublicKey:/x;$g;s/\n *//g;s/sshPublicKey: //gp')
uid=$(ldapsearch -x '(&(objectClass=posixAccount)(uid='"$1"'))' 'uidNumber' | sed -n '/^ /{H;d};/uidNumber:/x;$g;s/\n *//g;s/uidNumber: //gp')
if [ $uid -ge 2000 ]
then
	echo $key
else
	echo "UID incorrecto"
fi

