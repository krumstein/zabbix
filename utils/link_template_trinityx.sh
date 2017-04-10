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

get_template_id () {
echo $1 1>&2
result=$(curl -s localhost/zabbix/api_jsonrpc.php \
              -H 'Content-Type: application/json-rpc' \
              -d @- <<CURL_DATA
                {
                   "jsonrpc": "2.0",
                   "method": "template.get",
                   "params":
                    {
                       "output": "extend",
		       "filter": {
			    "host" : "$1"
        		}
                    },   
                   "auth": "${TOKEN}",
                   "id": 2
                 }
CURL_DATA
)
#echo $result | python -c "from __future__ import print_function;import sys, json,pprint; pprint.pprint(json.load(sys.stdin)['result'])" 

echo $result | python -c "from __future__ import print_function;import sys, json,pprint; print(json.load(sys.stdin)['result'][0]['templateid'],end='')" 
}

TEMPLATEID=$(get_template_id "CV TrinityX controller")
echo template_id $TEMPLATEID
result=$(curl -s localhost/zabbix/api_jsonrpc.php \
              -H 'Content-Type: application/json-rpc' \
              -d @- <<CURL_DATA
                {
                   "jsonrpc": "2.0",
                   "method": "template.update",
                   "params":
                    {
			"templateid": "$TEMPLATEID" ,
			"templates": [  {"templateid":"$(get_template_id 'CV App DRBD')"},  
					{"templateid":"$(get_template_id 'CV App Pacemaker')"}, 
					{"templateid":"$(get_template_id 'CV Slurm')"}]

                    },   
                   "auth": "${TOKEN}",
                   "id": 2
                 }
CURL_DATA
)
echo $result
