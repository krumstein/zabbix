#!/bin/bash
display_usage() {
        echo "This script add group"
        echo -e "\nUsage:\n$0 group \n"
        return 0
}
if [  $# -lt 1  ]
        then
                display_usage
                exit 1
fi

source /trinity/trinity.shadow
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
echo "adding group"
GROUP=$1
curl -s localhost/zabbix/api_jsonrpc.php \
              -H 'Content-Type: application/json-rpc' \
              -d @- <<CURL_DATA
                {
                   "jsonrpc": "2.0",
                   "method": "hostgroup.create",
                   "params":
                    {
                       "name":"${GROUP}"
                    },   
                   "auth": "${TOKEN}",
                   "id": 2
                 }
CURL_DATA

echo ""
