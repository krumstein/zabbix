Name:		cv-zabbix-checks	
Version:	0.35
Release:	0%{?dist}
Summary:	Zabbix checks by ClusterVision

Group:		CV	
License:	GPLv3.0
URL:		http://github.com/krumstein/zabbix
Source0:	%name-%version.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	zabbix-agent
%description
ClusterVision Zabbix checks

%prep
%setup -q


%build

%install
install -m 0755 -d $RPM_BUILD_ROOT/var/lib/zabbix
install -m 0755 -d $RPM_BUILD_ROOT/var/lib/zabbix/userparameters
install -m 0755 userparameters/* $RPM_BUILD_ROOT/var/lib/zabbix/userparameters/

install -m 0755 -d $RPM_BUILD_ROOT/etc/zabbix/zabbix_agentd.d/
install -m 0644 zabbix_agentd.d/* $RPM_BUILD_ROOT/etc/zabbix/zabbix_agentd.d/

install -m 0755 -d $RPM_BUILD_ROOT/etc/sudoers.d/
install -m 0644 sudoers-zabbix $RPM_BUILD_ROOT/etc/sudoers.d/zabbix

install -m 0755 -d $RPM_BUILD_ROOT/usr/lib/zabbix/templates/
install -m 0644  templates/*.xml $RPM_BUILD_ROOT/usr/lib/zabbix/templates/

install -m 0755 -d $RPM_BUILD_ROOT/usr/lib/zabbix/utils
install -m 0755 utils/*.sh $RPM_BUILD_ROOT/usr/lib/zabbix/utils/

install -m 0755 -d $RPM_BUILD_ROOT/usr/lib/zabbix/utils/gpfs_snmp
install -m 0755 utils/gpfs_snmp/* $RPM_BUILD_ROOT/usr/lib/zabbix/utils/gpfs_snmp/


install -m 0755 -d $RPM_BUILD_ROOT/usr/lib/zabbix/externalscripts/
install -m 0755 externalscripts/* $RPM_BUILD_ROOT/usr/lib/zabbix/externalscripts/

install -m 0755 -d   $RPM_BUILD_ROOT/etc/cron.d/
install -m 0644 gpfs_fileset_usage  $RPM_BUILD_ROOT/etc/cron.d/

install -m 0755 -d   $RPM_BUILD_ROOT/usr/lib/zabbix/ansible
install -m 0755 -d   $RPM_BUILD_ROOT/usr/lib/zabbix/ansible/library
install -m 0644 ansible/*.yml $RPM_BUILD_ROOT/usr/lib/zabbix/ansible
install -m 0644 ansible/library/* $RPM_BUILD_ROOT/usr/lib/zabbix/ansible/library



mkdir $RPM_BUILD_ROOT/tmp
touch $RPM_BUILD_ROOT/tmp/ipmitool.cache
touch $RPM_BUILD_ROOT/tmp/gpfs_filset_usage


%clean
rm -rf $RPM_BUILD_ROOT
%post
systemctl restart zabbix-agent


%files
%dir %attr(-,zabbix,zabbix) /var/lib/zabbix/userparameters
%attr(-,zabbix,zabbix) /var/lib/zabbix/userparameters/*

%attr(-,root,root) /etc/zabbix/zabbix_agentd.d/*

%attr(-,root,root) /etc/sudoers.d/zabbix
%attr(-,root,root) /usr/lib/zabbix/externalscripts/*
%attr(-,root,root) /tmp/ipmitool.cache
%attr(-,root,root) /tmp/gpfs_filset_usage
%attr(-,root,root) /usr/lib/zabbix/templates/*
%attr(-,root,root) /usr/lib/zabbix/utils/*
%attr(-,root,root) /usr/lib/zabbix/ansible/*
%config(noreplace) /etc/cron.d/gpfs_fileset_usage

%doc



%changelog
* Mon May 01 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.35.0
- Added disk monitoring for storcli
* Mon May 01 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.34.0
- Added ansible module
* Tue Apr 11 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.33.1
- Fixed gpfs_snmp installation
* Tue Apr 11 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.33.0
- Utils are now installed
* Mon Apr 10 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.32.0
- Fixed Zabbix templates: they're imported without errors
- Added a scripts to link a templates to another template
- Added a script to make agent listen for any controller IP
- Added a script to change auto registration action
* Fri Apr 07 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.31.0
- Fixed export script ( encoding problem ) and ansible .yml for SNMP configure of GPFS
* Fri Apr 07 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.30.0
- Added external check for ipmi and added check for amount of nodes of a slurm job
* Fri Apr 07 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.29.0
- Added checks for rsnapshot and amount of filehandles
* Fri Apr 07 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.28.0
- Zabbix agent does not log sudo
* Fri Apr 07 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.27.0
- Added templates
* Mon Feb 20 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.26.0
- Added template for IPMI on Huawei nodes, IPMItool no more return 'na' if there is no data for critical values, IPMItool by default support  filters
* Mon Feb 20 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.25.2
- Bugfix for ipmitool
* Fri Feb 17 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.25.1
- Bugfix for ipmitool
* Fri Feb 17 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.25.0
- Added support for ipmitool filter in macros and added ipmitool template for power nodes
* Fri Feb 17 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.24.2
- Make ipmitool external check for JBOD to take password from trinity.shadow
* Fri Feb 17 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.24.1
- Fixed rpmsdiff external check for newer pcs
* Fri Feb 17 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.24.0
- Added a ipmitool external checks for JBODs
* Tue Feb 14 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.23.1
- Hostname of HA Mellanox SM is in item key, not in external script
* Tue Feb 14 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.23.0
- Added check HA subnet manager on mellanox switches 
* Tue Feb 14 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.22.0
- Added check for errors on IB port
* Tue Feb 14 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.21.2
- Fixed name of userparameter configuration of sas3ircu and storcli
* Mon Feb 13 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.21.1
- Fixed APC InRow cooling template
* Mon Feb 13 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.21.0
- Added export.sh script,fixed ipmitool template and fixed import.sh for newer TrinityX version
* Fri Feb 10 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.20.0
- Added infiniband checks
* Fri Feb 10 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.19.0
- Added huawei sel check
* Fri Feb 10 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.18.0
- Added mysql galera check
* Fri Feb 10 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.17.1
- Added sas2ircu check
* Fri Feb 10 2017 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.17.0
- Added sas2ircu check
* Tue Dec 13 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.16.3
- GPFS fileset usage reports even without quotas.
* Mon Dec 12 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.16
- Added standart node template.
* Mon Dec 05 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.14
- Added OPAinfo bandwidth monitoring.
* Fri Dec 02 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.13
- Added mysql slave monitoring.
* Fri Dec 02 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.12
- Added slurm node status and count of jobs monitoring, move slurm daemon to slurm node 
* Fri Dec 02 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.11
- Added rpm package difference between controller nodes
* Tue Nov 29 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.10
- Added verbose linux memory monitoring and graph
* Thu Nov 17 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.9
- Updated templates, standart timeouts
* Tue Nov 15 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.8
- Added storcli
* Tue Nov 15 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.7
- Added sas3ircu and simplified spec file
* Thu Nov 10 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.6
- Added add_group.sh script and moved import.sh to utils directory
* Fri Nov 04 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.5.3
- Added opa hfi monitoring
* Fri Nov 04 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.5.1
- Added accessibilty of mount check
* Fri Nov 04 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.5
- Added mounts checks via systemd
* Fri Oct 28 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.1
- Initial RPM release 
* Fri Oct 28 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.2
- Added external checks
