import SoftLayer
from SoftLayer import utils
import sys
import pprint
import logging



pp = pprint.PrettyPrinter(indent=4)
client = SoftLayer.Client(username=apiUsername,api_key=apiKey)

mask = "mask[]"


test1 = client['SoftLayer_Ticket'].getObject(id=9675518)


pp.pprint(test1)
