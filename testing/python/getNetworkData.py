import SoftLayer
from SoftLayer import utils
import sys
import pprint


apiUsername = 'xxx'
apiKey = 'xxx'
pp = pprint.PrettyPrinter(indent=4)


client = SoftLayer.Client(username=apiUsername,api_key=apiKey)
mask = "mask[primarySubnet,networkSpace]"
result = client['SoftLayer_Account'].getNetworkVlans(mask=mask)
pp.pprint(result)
