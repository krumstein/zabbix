#!/bin/bash
display_usage() { 
	echo "This script exports template from local zabbix server" 
	echo -e "\nUsage:\n$0 template id \n" 
	return 0
} 
if [  $# -lt 1  ] 
	then 
		display_usage
		exit 1
fi 


TEMPLATE_ID=$1
source /trinity/local/trinity.shadow
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
result=$(curl -s localhost/zabbix/api_jsonrpc.php \
              -H 'Content-Type: application/json-rpc' \
              -d @- <<CURL_DATA
 {"jsonrpc": "2.0",
                   "method": "configuration.export",
                  "params": {
                       "format": "xml",
			"options": {
            			"templates": [
                			"${TEMPLATE_ID}"
            			]
        		}
				
                       
                   },
                   "auth": "${TOKEN}",
                   "id": 2
	         }  
CURL_DATA
)
echo $result |  python -c "import sys, json; print  str(json.load(sys.stdin)['result'].encode('utf-8'))" | xmllint --format -
