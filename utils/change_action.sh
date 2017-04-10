#!/bin/bash
source /trinity/local/trinity.shadow
echo "getting token"
TOKEN=$(curl -s localhost/zabbix/api_jsonrpc.php \
              -H 'Content-Type: application/json-rpc' \
              -d '{"jsonrpc": "2.0",
                   "method": "user.login",
                   "auth": null,
                   "id": 1,
                   "params": {
                        "user": "Admin",
                        "password": "'${ZABBIX_ADMIN_PASSWORD}'"
                   }}'  | python -c "import json,sys; auth=json.load(sys.stdin); print (auth[\"result\"])")
echo "Got token"
result=$(curl -s localhost/zabbix/api_jsonrpc.php \
              -H 'Content-Type: application/json-rpc' \
              -d @- <<CURL_DATA
                {
                   "jsonrpc": "2.0",
                   "method": "action.get",
                   "params":
                    {
                       "output": "extend",
        		"selectOperations": "extend",
		        "selectRecoveryOperations": "extend",
		        "selectFilter": "extend",
		        "filter": {
			    "name" : "Auto registration"
        		}
                    },   
                   "auth": "${TOKEN}",
                   "id": 2
                 }
CURL_DATA
)
#echo $result
#echo $result | python -c "from __future__ import print_function;import sys, json,pprint; pprint.pprint(json.load(sys.stdin)['result'])" 

ACTIONID=$(echo $result | python -c "from __future__ import print_function;import sys, json,pprint; print(json.load(sys.stdin)['result'][0]['actionid'],end='')" )
#echo $ACTIONID
result=$(curl -s localhost/zabbix/api_jsonrpc.php \
              -H 'Content-Type: application/json-rpc' \
              -d @- <<CURL_DATA
                {
                   "jsonrpc": "2.0",
                   "method": "action.update",
                   "params":
                    {
			"actionid": $ACTIONID ,
			"operations": [ {
				"actionid": $ACTIONID ,
                   "esc_period": "0",
                   "esc_step_from": "1",
                   "esc_step_to": "1",
                   "evaltype": "0",
                   "opconditions": [],
                   "operationid": "13",
                   "operationtype": "6",
                   "optemplate": [  {"operationid": "13",
                                    "templateid": "10102"},
                                   {"operationid": "13",
                                    "templateid": "10104"}],
                   "recovery": "0"	
					} ]
                    },   
                   "auth": "${TOKEN}",
                   "id": 2
                 }
CURL_DATA
)

echo $result
