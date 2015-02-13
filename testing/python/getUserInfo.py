import SoftLayer
import pprint


pp = pprint.PrettyPrinter(indent=4)
client = SoftLayer.Client(username=apiUsername,api_key=apiKey)

api_mask = "mask[id,apiAuthenticationKeys,username]"
user = client['SoftLayer_Brand'].getUsers(id=4644,mask=api_mask)

pp.pprint(user)

