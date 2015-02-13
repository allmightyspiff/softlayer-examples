import SoftLayer
from SoftLayer import utils
import sys
import pprint


pp = pprint.PrettyPrinter(indent=4)
client = SoftLayer.Client(username=apiUsername,api_key=apiKey)

_filter = {}
_filter['partitionTemplates'] = {}
_filter['partitionTemplates']['description'] = utils.query_filter('*= cPanel')
pp.pprint(_filter)
result = client['SoftLayer_Hardware_Component_Partition_OperatingSystem'].getPartitionTemplates(id=1,filter=_filter)
pp.pprint(result)
