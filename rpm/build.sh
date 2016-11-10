#!/bin/bash
set -e
VERSION=$(grep Version zabbix-checks.spec | awk '{print $2}')
NAME=$(grep Name zabbix-checks.spec | awk '{print $2}')
SRCDIR=~/rpmbuild/SOURCES/${NAME}-${VERSION}
TARNAME=${NAME}-${VERSION}.tar.gz

if [ -e ${SRCDIR} ]
then
	rm -rf  ${SRCDIR}
fi
echo ~
echo $SRCDIR
mkdir $SRCDIR
cp -rf ../* ${SRCDIR}
cd ~/rpmbuild/SOURCES/
if [ -e $TARNAME ]
then
	rm -rf  $TARNAME
fi

tar czvf $TARNAME ${NAME}-${VERSION}
cd -
rpmbuild -bs zabbix-checks.spec
