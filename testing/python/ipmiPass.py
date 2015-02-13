import SoftLayer
from SoftLayer import utils
import sys
import pprint
import logging



pp = pprint.PrettyPrinter(indent=4)
client = SoftLayer.Client(username=apiUsername,api_key=apiKey)

mask = "mask[consoleIpAddressRecord[ipAddress]]"

result = client['SoftLayer_Account'].getVirtualGuests(mask=mask)

pp.pprint(result)
