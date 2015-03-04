# So we can talk to the SoftLayer API:
import SoftLayer.API
from SoftLayer import VSManager
# For nice debug output:
from pprint import pprint as pp


def create_user(username):
    password = "THIS15dev@"
    user_template = {
        'username': username,
        'firstName': 'Impact User',
        'lastName': 'Impact User',
        'email': 'pjackson@softlayer.com',
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


def list_users():
    from prettytable import PrettyTable
    table = PrettyTable(['Username', 'Password', 'ID'])
    users = client['Account'].getUsers()
    for user in users:
        if 'dev-at' not in user['username']:
            continue
        else:
            table.add_row([user['username'], 'devat-', user['id']])

    print table
    exit()


def fix_permissions(user,permissions):
    t = user['id']
    set_permissions(user['id'], permissions)
    client['User_Customer'].removeAllVirtualAccessForThisUser(id=t)
    client['User_Customer'].removeAllHardwareAccessForThisUser(id=t)
    client['User_Customer'].addApiAuthenticationKey(id=t)

def orderUserServer(user, apiKey):
    hostname = "salt-master"
    guest = {}
    guest['startCpus'] = 1
    guest['maxMemory'] = 1024
    guest['localDiskFlag'] = False
    guest['hostname'] = hostname
    guest['domain'] = user + ".lablayer.info"
    guest['hourlyBillingFlag'] = True
    guest['datacenter'] = {}
    guest['datacenter']['name'] = 'sjc01'
    #guest['blockDeviceTemplateGroup'] = {'globalIdentifier': "9412b820-0cc7-493d-a38b-e3ef44733da2"}
    #guest['blockDeviceTemplateGroup'] = {'globalIdentifier': "f9db594e-c4c1-489d-870a-572bbd25f734"}
    #v12
    guest['blockDeviceTemplateGroup'] = {'globalIdentifier': "96fcb150-1159-4e91-bbff-82aedfae11f4"}

    userClient = SoftLayer.Client(
        username = user,
        api_key = apiKey )
    result = userClient['Virtual_Guest'].createObject(guest)
    print "Added server id: %s  ( %s )" % (result['id'],result['fullyQualifiedDomainName']) 
    return


if __name__ == "__main__":
    import argparse
    argsparse = argparse.ArgumentParser(description='Number of users')
    argsparse.add_argument('--num-users', dest='num_users', type=int,
                           help='Number of users to provision.')
    argsparse.add_argument('--list', action='store_true',
                           help='List lab users', default=False)
    argsparse.add_argument('--offset', dest="offset", type=int,
                           default=1, help='Username offset')
 
    args = argsparse.parse_args()
    template_user_id = 264562
    api_username = ''
    api_key = ''
    client = SoftLayer.Client(
        username=api_username,
        api_key=api_key,
    )

    if args.list is True:
        list_users()

    
    userPerms = client['User_Customer'].getPermissions(id=template_user_id)
   
    start_user_num = args.offset

    for i in range(args.num_users):
        target_username = 'devat-%s' % (start_user_num)
        new_user = create_user(target_username)
        fix_permissions(new_user,userPerms)
        newApiKey = client['User_Customer'].getApiAuthenticationKeys(id=new_user['id'])
        print "username = %s" % (newApiKey[0]['user']['username'])
        print "api_key =  %s" % (newApiKey[0]['authenticationKey'])
        orderUserServer(newApiKey[0]['user']['username'],newApiKey[0]['authenticationKey'])
        start_user_num = start_user_num + 1
        print "Created user: %s" % (target_username)
