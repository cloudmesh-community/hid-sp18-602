from os import environ as env
from credentials import get_keystone_creds
import keystoneclient.v2_0.client as ksclient
import glanceclient


def get_images_list():
 
    creds =get_keystone_creds()
    keystone=ksclient.Client(**creds)
    glance_endpoint = keystone.service_catalog.url_for(service_type='image', endpoint_type='public')
    glance = glclient.Client(glance_endpoint, token=keystone.auth_token)
    images = glance.images.list()
    detailed_list =list(images)
    images_name=[]
    for x in detailed_list:
	if(x["status"]=="active" and x["visibility"]=="public"):
	   images_name.append([x["name"],x["id"]])
    images_name.sort()
    return images_name
    
