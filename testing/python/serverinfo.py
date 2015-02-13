import SoftLayer
from SoftLayer import utils
import sys
import pprint



server = 132672 
pp = pprint.PrettyPrinter(indent=4)
client = SoftLayer.Client(username=apiUsername,api_key=apiKey)


mask = "mask[lastTransaction[transactionGroup]]"

result = client['SoftLayer_Hardware_Server'].getObject(mask=mask,id=server)

pp.pprint(result)
