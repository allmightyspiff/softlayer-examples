import SoftLayer
from SoftLayer import utils
import pprint


pp = pprint.PrettyPrinter(indent=4)
client = SoftLayer.Client(username=apiUsername,api_key=apiKey)

api_mask = "mask[id,username,billingItem[id,orderItemId]]"
api_filter = {'id' : {'operation':4309650}}

_filter = {}
_filter['hubNetworkStorage'] = {} 
_filter['hubNetworkStorage']['id'] = utils.query_filter('*= 4309650')

result = client['SoftLayer_Account'].getHubNetworkStorage(mask=api_mask,filter=_filter)


pp.pprint(result)
