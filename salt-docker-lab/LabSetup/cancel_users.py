# So we can talk to the SoftLayer API:
import SoftLayer.API
# For nice debug output:
from pprint import pprint as pp


def get_target_users(prefix):
    _filter = {
        'users': {
            'username': {
                'operation': '*= %s' % (prefix)
            }
        }
    }

    _mask = "mask[id,username]"

    _users = client['Account'].getUsers(filter=_filter, mask=_mask)
    return _users

def get_target_keys(prefix):
    _filter = {
        'sshKeys': {
            'label': {
                'operation': '*= %s' % (prefix)
            }
        }
    }

    _mask = "mask[id,label]"

    _users = client['Account'].getSshKeys(filter=_filter, mask=_mask)
    return _users

def print_result(result, thing):
    if result == True:
        print "\033[42;97mOK\033[0m"
    else:
        print "\033[31mERROR: "
        pp(thing)
        print "\033[0m"

    return


if __name__ == "__main__":
    import argparse
    argsparse = argparse.ArgumentParser(description='Number of users')
    argsparse.add_argument('--prefix',
                           help='Username prefix', default=False)
 
    args = argsparse.parse_args()

    ##### CHANGE THESE #################
    api_username = ''
    api_key = ''
    ####################################

    client = SoftLayer.Client(
        username=api_username,
        api_key=api_key,
    )
  
    users = get_target_users(args.prefix)

    for user in users:
        print '\033[95mUser: ' + user['username'] + '\033[0m'
        template = {
            'id': user['id'],
            'userStatusId': 1021
        }
        servers = client['User_Customer'].getVirtualGuests(id=user['id'])
        result = True
        for virt in servers: 
            print("\tCanceling host... \033[34m" + virt['fullyQualifiedDomainName'] + " \033[96m(" + str(virt['id']) + ")\t\033[0m"),
            try:
                result = client['Virtual_Guest'].deleteObject(id=virt['id'])
                print_result(result,virt)
            except SoftLayer.exceptions.SoftLayerAPIError as error:
                print("\t\033[31mException, host might already be canceling...\033[0m")
                pp(error)

        print("\tRemoving user... \033[34m" + user['username'] + " \033[96m(" + str(user['id']) + ")\t\033[0m"),
        result = client['User_Customer'].editObject(template, id=user['id'])
        print_result(result,user)
 
    sshkeys = get_target_keys(args.prefix)
    print '\033[95mSSH Key Removal\033[0m'
    for key in sshkeys:
        print("Deleting key... \033[34m" + key['label'] + " \033[96m(" + str(key['id']) + ")\t\033[0m"),
        result = client['SoftLayer_Security_Ssh_Key'].deleteObject(id=key['id'])
        print_result(result,key)


    print '\033[94mComplete'
    print '\033[0m' 