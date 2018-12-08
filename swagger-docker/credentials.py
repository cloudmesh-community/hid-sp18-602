#!/usr/bin/env python
import os
 
def get_keystone_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_name']=os.environ['OS_PROJECT_NAME']
    d['project_id']=os.environ['OS_PROJECT_ID']
    d['identity_version']=os.environ['OS_IDENTITY_API_VERSION']
	
    return d
