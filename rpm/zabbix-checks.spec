Name:		cv-zabbix-checks	
Version:	0.20
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
install -m 0755 utils/import.sh $RPM_BUILD_ROOT/usr/lib/zabbix/utils/
install -m 0755 utils/add_group.sh $RPM_BUILD_ROOT/usr/lib/zabbix/utils/


install -m 0755 -d $RPM_BUILD_ROOT/usr/lib/zabbix/externalscripts/
install -m 0755 externalscripts/* $RPM_BUILD_ROOT/usr/lib/zabbix/externalscripts/

install -m 0755 -d   $RPM_BUILD_ROOT/etc/cron.d/
install -m 0644 gpfs_fileset_usage  $RPM_BUILD_ROOT/etc/cron.d/


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
%config(noreplace) /etc/cron.d/gpfs_fileset_usage

%doc



%changelog
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

