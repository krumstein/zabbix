#!/usr/bin/python

from  ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.pycompat24 import get_exception
import json
import datetime
import logging
import copy
import pprint
try:
    from zabbix_api import ZabbixAPI, ZabbixAPISubClass

    HAS_ZABBIX_API = True
except ImportError:
    HAS_ZABBIX_API = False


def main():
    module = AnsibleModule(
        argument_spec = dict(
            username      = dict(required=True),
            password      = dict(required=True),
            hostname      = dict(required=True),
            object        = dict(required=True),
            action        = dict(required=True),
            params        = dict(default={},type="dict" )
            )
    )
    date = str(datetime.datetime.now())

    zapi = ZabbixAPI('http://{}/zabbix'.format(module.params['hostname'] ))

    zapi.login(module.params['username'], module.params['password'])
    object = getattr(zapi, module.params['object'])
    method = getattr(object, module.params['action'])
    result =  method(module.params['params'])
    module.exit_json(changed=True, result=result)
 
if __name__ == '__main__':  
    main()
