import keystoneclient.v2_0.client as ksclient
from credentials import get_keystone_creds
creds = get_keystone_creds()
keystone = ksclient.Client(**creds)
print keystone.auth_token
