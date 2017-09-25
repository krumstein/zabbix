#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.pycompat24 import get_exception
import json
from zabbix_api import ZabbixAPI, ZabbixAPISubClass, ZabbixAPIException



def main():
    module = AnsibleModule(
        argument_spec = dict(
            username      = dict(required=True),
            password      = dict(required=True),
            hostname      = dict(required=True),
            object        = dict(required=True),
            action        = dict(required=True),
            params        = dict(default={},type="dict" ),
            query         = dict(type="dict"),
            )
    )
    try:
        zapi = ZabbixAPI('http://{}/zabbix'.format(module.params['hostname'] ),timeout=120)
        zapi.login(module.params['username'], module.params['password'])
        object = getattr(zapi, module.params['object'])
        result=[]
        msg = []
        if module.params['action'] == "find_update":        
            found_objects = object.get({'filter':module.params['query']})
            msg.append(found_objects)
            if len(found_objects) == 0 :
                module.fail_json("Could not find object")
            else:
                map(lambda x: result.append(object.update(dict({k:v for k,v in x.items() if k.endswith('id')}, **module.params['params']))),found_objects)
        elif module.params['action'] == "find_delete":
            found_objects = object.get({'filter':module.params['query']})
            msg.append(found_objects)
            if len(found_objects) == 0 :
                module.fail_json("Could not find object")
            else:
                map(lambda x: result.append(object.delete(dict({k:v for k,v in x.items() if k.endswith('id')})),found_objects))

        elif module.params['action'] == 'create':
            try:
                method = getattr(object, module.params['action'])
                result =  method(module.params['params'])
            except ZabbixAPIException as e:
                if "already exists." in str(e):
                    module.exit_json(changed=False,  result=result,msg=msg)
                else:
                    module.fail_json(msg="Zabbix API exception:{}".format(e))
        else:
            method = getattr(object, module.params['action'])
            result =  method(module.params['params'])
        module.exit_json(changed=True, result=result,msg=msg)
    except ZabbixAPIException as e:
        module.fail_json(msg="Zabbix API exception:{}".format(e))
 
if __name__ == '__main__':  
    main()
