## Bunch of zabbix checks and templates.
To install zabbix checks you need to pick an alredy built RPM or build a new one. To build an RPM:

```bash
cd rpm
./build.sh
rpmbuild --rebuild  ~/rpmbuild/SRPMS/cv-zabbix-checks-0.9*.src.rpm
```

###GPFS:
Just follow http://www.ibm.com/developerworks/library/l-snmp-gpfs/
On the collector node edit the /etc/snmp/snmpd.conf:
```
	master agentx
	trap2sink admin
	AgentXSocket tcp:localhost:705
	AgentXTimeout 20
	AgentXRetries 10

	rocommunity  public <IP ADDRESS OF ZABBIX SERVER>

	syslocation Unknown (edit /etc/snmp/snmpd.conf)

	syscontact Root <root@localhost> (configure /etc/snmp/snmp.local.conf)

	view    all            included      .1
	view    systemview    included   .1
	view    systemview    included   .1
	dontLogTCPWrappersConnects yes
	smuxpeer .1.3.6.1.4.1.674.10892.1
```
