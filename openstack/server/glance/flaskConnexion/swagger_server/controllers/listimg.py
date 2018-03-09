from os import environ as env
import keystoneclient.v2_0.client as ksclient
import glanceclient

def get_images_list():
 
    creds =get_keystone_creds()
    keystone=ksclient.Client(**creds)
    glance_endpoint = keystone.service_catalog.url_for(service_type='image',endpoint_type='publicURL')
    glance = glanceclient.Client('1',glance_endpoint, token=keystone.auth_token) 
    with open('cirros-0.4.0-x86_64-disk.img') as fimage: glance.images.create(name="cirros", is_public=True, disk_format="qcow2",
									      container_format="bare", data=fimage)
    glance = glanceclient.Client('2',glance_endpoint, token=keystone.auth_token)
    images = glance.images.list()
    return 0  
