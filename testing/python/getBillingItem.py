import SoftLayer
from SoftLayer import utils
import sys
import pprint
import logging


billingId = 54258848 

billingItemId = 42531892
pp = pprint.PrettyPrinter(indent=4)
client = SoftLayer.Client(username=apiUsername,api_key=apiKey)


mask = "mask[invoiceItems]"
output = client['SoftLayer_Billing_Order_Item'].getBillingItem(id=billingId,mask=mask)


pp.pprint(output)
