Bunch of zabbix checks and templates.
To install zabbix checks you need to pick an alredy built RPM or build a new one. You can find VERSION in spec. To build an RPM:
1. make a source directory 
	mkdir ~/rpmbuild/SOURCES/cv-zabbix-checks-<VERSION>
2. copy zabbix files to that directory
	


GPFS:
Just follow http://www.ibm.com/developerworks/library/l-snmp-gpfs/
On the collector node edit the /etc/snmp/snmpd.conf:
	master agentx
	trap2sink admin
	AgentXSocket tcp:localhost:705
	AgentXTimeout 20
	AgentXRetries 10
	com2sec notConfigUser  default       public
	group   notConfigGroup v1           notConfigUser
	group   notConfigGroup v2c           notConfigUser
	view    systemview    included   .1
	view    systemview    included   .1
	access  notConfigGroup ""      any       noauth    exact  systemview none none
	syslocation dumbo1.cluster
	syscontact Root <root@localhost>
	dontLogTCPWrappersConnects yes
	
