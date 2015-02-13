
import SoftLayer
import pprint
pp = pprint.PrettyPrinter(indent=2)


client = SoftLayer.Client(username=apiUsername,api_key=apiKey)

mask = "mask[networkVlans[primaryRouter[topLevelLocation]]]"

# result = client['SoftLayer_Virtual_Guest'].getObject(id=7521218,mask=mask)

result = client['SoftLayer_Network_Vlan'].getPrivateVlan(id=720664)

pp.pprint(result)
