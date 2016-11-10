Name:		cv-zabbix-checks	
Version:	0.6
Release:	1%{?dist}
Summary:	Zabbix checks by CLusterVision

Group:		CV	
License:	GPLv3.0
URL:		http://github.com/krumstein/trinityX
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
install -m 0755 userparameters/opainfo userparameters/mounts_systemd userparameters/smartctl-disks-discovery.pl userparameters/drbd   userparameters/ipmitool   userparameters/pacemaker   userparameters/perc   userparameters/smcli $RPM_BUILD_ROOT/var/lib/zabbix/userparameters/

install -m 0755 -d $RPM_BUILD_ROOT/etc/zabbix/zabbix_agentd.d/
install -m 0644 zabbix_agentd.d/userparameter_opainfo.conf  zabbix_agentd.d/userparameter_systemd.conf zabbix_agentd.d/userparameter_mounts_systemd.conf zabbix_agentd.d/userparameter_smartctl.conf zabbix_agentd.d/userparameter_drbd.conf   zabbix_agentd.d/userparameter_ipmi.conf   zabbix_agentd.d/userparameter_pacemaker.conf   zabbix_agentd.d/userparameter_perc.conf   zabbix_agentd.d/userparameter_smcli.conf  $RPM_BUILD_ROOT/etc/zabbix/zabbix_agentd.d/

install -m 0755 -d $RPM_BUILD_ROOT/etc/sudoers.d/
install -m 0644 sudoers-zabbix $RPM_BUILD_ROOT/etc/sudoers.d/zabbix

install -m 0755 -d $RPM_BUILD_ROOT/usr/lib/zabbix/templates/
install -m 0644  templates/opainfo.xml templates/slurm_daemon.xml  templates/chrony_daemon.xml templates/mounts_systemd.xml templates/smartctl.xml templates/apc_inrow_cooling.xml templates/drbd.xml templates/ipmitool.xml templates/pacemaker.xml templates/perc.xml templates/powervault.xml templates/slurm.xml templates/smcli.xml  $RPM_BUILD_ROOT/usr/lib/zabbix/templates/

install -m 0755 -d $RPM_BUILD_ROOT/usr/lib/zabbix/utils
install -m 0755 utils/import.sh $RPM_BUILD_ROOT/usr/lib/zabbix/utils/
install -m 0755 utils/add_group.sh $RPM_BUILD_ROOT/usr/lib/zabbix/utils/


install -m 0755 -d $RPM_BUILD_ROOT/usr/lib/zabbix/externalscripts/
install -m 0755 externalscripts/check_md_status  externalscripts/slurm $RPM_BUILD_ROOT/usr/lib/zabbix/externalscripts/
mkdir $RPM_BUILD_ROOT/tmp
touch $RPM_BUILD_ROOT/tmp/ipmitool.cache

%clean
rm -rf $RPM_BUILD_ROOT
%post
systemctl restart zabbix-agent


%files
%dir %attr(-,zabbix,zabbix) /var/lib/zabbix/userparameters
%attr(-,zabbix,zabbix) /var/lib/zabbix/userparameters/drbd
%attr(-,zabbix,zabbix) /var/lib/zabbix/userparameters/ipmitool
%attr(-,zabbix,zabbix) /var/lib/zabbix/userparameters/pacemaker
%attr(-,zabbix,zabbix) /var/lib/zabbix/userparameters/perc
%attr(-,zabbix,zabbix) /var/lib/zabbix/userparameters/smcli
%attr(-,zabbix,zabbix) /var/lib/zabbix/userparameters/mounts_systemd
%attr(-,zabbix,zabbix) /var/lib/zabbix/userparameters/opainfo
%attr(-,zabbix,zabbix) /var/lib/zabbix/userparameters/smartctl-disks-discovery.pl

%attr(-,root,root) /etc/zabbix/zabbix_agentd.d/userparameter_drbd.conf
%attr(-,root,root) /etc/zabbix/zabbix_agentd.d/userparameter_ipmi.conf
%attr(-,root,root) /etc/zabbix/zabbix_agentd.d/userparameter_pacemaker.conf
%attr(-,root,root) /etc/zabbix/zabbix_agentd.d/userparameter_perc.conf
%attr(-,root,root) /etc/zabbix/zabbix_agentd.d/userparameter_smcli.conf
%attr(-,root,root) /etc/zabbix/zabbix_agentd.d/userparameter_mounts_systemd.conf
%attr(-,root,root) /etc/zabbix/zabbix_agentd.d/userparameter_systemd.conf
%attr(-,root,root) /etc/zabbix/zabbix_agentd.d/userparameter_opainfo.conf
%attr(-,root,root) /etc/zabbix/zabbix_agentd.d/userparameter_smartctl.conf

%attr(-,root,root) /etc/sudoers.d/zabbix
%attr(-,root,root) /usr/lib/zabbix/externalscripts/check_md_status
%attr(-,root,root) /usr/lib/zabbix/externalscripts/slurm
%attr(-,root,root) /tmp/ipmitool.cache
%attr(-,root,root) /usr/lib/zabbix/templates/apc_inrow_cooling.xml
%attr(-,root,root) /usr/lib/zabbix/templates/drbd.xml
%attr(-,root,root) /usr/lib/zabbix/templates/ipmitool.xml
%attr(-,root,root) /usr/lib/zabbix/templates/pacemaker.xml
%attr(-,root,root) /usr/lib/zabbix/templates/perc.xml
%attr(-,root,root) /usr/lib/zabbix/templates/powervault.xml
%attr(-,root,root) /usr/lib/zabbix/templates/slurm.xml
%attr(-,root,root) /usr/lib/zabbix/templates/smcli.xml
%attr(-,root,root) /usr/lib/zabbix/templates/mounts_systemd.xml
%attr(-,root,root) /usr/lib/zabbix/templates/slurm_daemon.xml
%attr(-,root,root) /usr/lib/zabbix/templates/chrony_daemon.xml
%attr(-,root,root) /usr/lib/zabbix/templates/smartctl.xml
%attr(-,root,root) /usr/lib/zabbix/templates/opainfo.xml                                                          

%attr(-,root,root) /usr/lib/zabbix/utils/import.sh
%attr(-,root,root) /usr/lib/zabbix/utils/add_group.sh

%doc



%changelog
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

