import SoftLayer
from SoftLayer import utils
import sys
import pprint
import logging


server = 132672 
pp = pprint.PrettyPrinter(indent=4)
client = SoftLayer.Client(username=apiUsername,api_key=apiKey)

mask = "mask[attributes]"


metadata = '123, 456, 789'
test1 = client['SoftLayer_Hardware_Server'].setUserMetadata({'value': 'tttttt'},id=server)

result = client['SoftLayer_Hardware_Server'].getObject(mask=mask,id=server)

pp.pprint(result)
