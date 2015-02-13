# So we can talk to the SoftLayer API:
import SoftLayer.API
from SoftLayer import VSManager
# For nice debug output:
from pprint import pprint as pp


userClient = SoftLayer.Client(username = api_username,  api_key = api_key )
guest = {}
guest['startCpus'] = 1
guest['maxMemory'] = 1024
guest['localDiskFlag'] = False
guest['hostname'] = 'partition-test'
guest['domain'] = 'cgallo.com'
guest['hourlyBillingFlag'] = True
guest['datacenter'] = {}
guest['datacenter']['name'] = 'sjc01'
guest['blockDevices'] = {'device' : 0}

# result = userClient['Virtual_Guest'].createObject(guest)

result = userClient['SoftLayer_Hardware_Component_Partition_OperatingSystem'].getPartitionTemplates(id=1)

pp(result)
