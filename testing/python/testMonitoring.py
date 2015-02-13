import SoftLayer
import pprint
pp = pprint.PrettyPrinter(indent=2)

#comma seperated list of ids
serverId = 153015


client = SoftLayer.Client(username=apiUsername,api_key=apiKey)

mgr = SoftLayer.HardwareManager(client)
nmgr = SoftLayer.NetworkManager(client)


status = client['Account'].getNextInvoiceTotalAmount()
pp.pprint(status)




