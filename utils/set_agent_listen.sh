#!/bin/bash
source /etc/trinity.sh;  sed -i "s/Server=.*/Server=${TRIX_CTRL1_IP},${TRIX_CTRL2_IP},${TRIX_CTRL_IP}/" /etc/zabbix/zabbix_agentd.conf
source /etc/trinity.sh;  sed -i "s/ServerActive=.*/ServerActive=${TRIX_CTRL1_IP},${TRIX_CTRL2_IP},${TRIX_CTRL_IP}/" /etc/zabbix/zabbix_agentd.conf
systemctl restart zabbix-agent
