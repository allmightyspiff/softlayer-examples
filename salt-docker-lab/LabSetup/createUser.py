# So we can talk to the SoftLayer API:
import SoftLayer.API
from SoftLayer import VSManager
# For nice debug output:
from pprint import pprint as pp


def create_user(username):
    password = 'SL<3sSingapore!'
    user_template = {
        'username': username,
        'firstName': 'Impact User',
        'lastName': 'Impact User',
        'email': 'someone@somewhere.com',
        'companyName': 'IBM Impact Lab',
        'address1': '3355 S Las Vegas Blvd',
        'city': 'Las Vegas',
        'country': 'US',
        'postalCode': 'NV 89109',
        'userStatusId': 1001,
        'timezoneId': 107
    }
    created_user = client['User_Customer'].createObject(
        user_template,
        password,
        password)
    return created_user

def get_permissions(_id):
    permissions = client['User_Customer'].getPermissions(id=_id)
    return permissions

def set_permissions(_id, permissions):
    return client['User_Customer'].addBulkPortalPermission(
        permissions, id=_id)

def fix_permissions(user,permissions):
    t = user['id']
    set_permissions(user['id'], permissions)
    client['User_Customer'].removeAllVirtualAccessForThisUser(id=t)
    client['User_Customer'].removeAllHardwareAccessForThisUser(id=t)
    client['User_Customer'].addApiAuthenticationKey(id=t)


##### CHANGE THESE #################
template_user_id = 264562
api_username = ''
api_key = ''
####################################
client = SoftLayer.Client(
    username=api_username,
    api_key=api_key,
)


userPerms = client['User_Customer'].getPermissions(id=template_user_id)


target_username = 'tokyo-lab'
new_user = create_user(target_username)
fix_permissions(new_user,userPerms)
newApiKey = client['User_Customer'].getApiAuthenticationKeys(id=new_user['id'])
print "username = %s" % (newApiKey[0]['user']['username'])
print "api_key =  %s" % (newApiKey[0]['authenticationKey'])
print "Created user: %s" % (target_username)
