# So we can talk to the SoftLayer API:
import SoftLayer.API
from SoftLayer import VSManager
# For nice debug output:
from pprint import pprint as pp



api_username = 'USERNAME'
api_key = 'APIKEY'
client = SoftLayer.Client(
    username=api_username,
    api_key=api_key,
)

guest = {}
guest['startCpus'] = 1
guest['maxMemory'] = 1024
guest['localDiskFlag'] = False
guest['hostname'] = "salt-master"
guest['domain'] =  "cgallo.lablayer.info"
guest['hourlyBillingFlag'] = True
guest['datacenter'] = {}
guest['datacenter']['name'] = 'sjc01'
guest['blockDeviceTemplateGroup'] = {'globalIdentifier': "8fbf5718-6897-434f-9840-6a09198e242a"}
result = client['Virtual_Guest'].createObject(guest)
print "Added server id: %s  ( %s )" % (result['id'],result['fullyQualifiedDomainName']) 
