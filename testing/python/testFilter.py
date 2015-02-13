import SoftLayer
from SoftLayer import utils
import sys
import pprint




pp = pprint.PrettyPrinter(indent=4)
client = SoftLayer.Client(username=apiUsername,api_key=apiKey)


items = ['invoices']
theMask  = "mask[%s]" % ','.join(items)
theFilter = {
        'invoices': {
            'createDate': {
                'operation': 'betweenDate',
                'options': [
                    {'name': 'startDate', 'value': ['2014-11-01T09:30:53-07:00']},
                    {'name': 'endDate', 'value': ['2014-12-01T09:30:53-07:00']}
                ]
            }
        }
    }

result = client['SoftLayer_Account'].getInvoices( filter=theFilter);
pp.pprint(result)
