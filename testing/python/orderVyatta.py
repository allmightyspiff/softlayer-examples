import SoftLayer
from SoftLayer import utils
import sys
import pprint
import logging


# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

logging.debug("Starting up")
pp = pprint.PrettyPrinter(indent=4)
client = SoftLayer.Client(username=apiUsername,api_key=apiKey)





productOrder = {'orderContainers': [
        {'hardware': 
            [
                {'domain': u'cr02a.dal05.com',
                 'hostname': u'cgallo-vyatta',
                 #Private VLAN 1147 on bcr02a.dal05
                 'primaryBackendNetworkComponent': {'networkVlanId': 557986},
                 #Public VLAN 1425 on fcr02a.dal05
                 'primaryNetworkComponent': {'networkVlanId': 557984}
                }
            ],
            'location': 138124,
            'packageId': 174,
            'prices': [
                {'id': 13738}, {'id': 36044}, {'id': 21010},
                {'id': 876}, {'id': 1267}, {'id': 342},
                {'id': 273}, {'id': 906}, {'id': 21},
                {'id': 17129}, {'id': 55}, {'id': 57},
                {'id': 58}, {'id': 420}, {'id': 418}
            ],
            'quantity': 1
        }
    ]
}

accountClient = client['SoftLayer_Account']
gatewayClient = client['SoftLayer_Network_Gateway']

# gateway = gatewayClient.getObject(id=31882,mask='insideVlans[networkVlan[vlanNumber]]')
gateway = accountClient.getNetworkGateways();

# vlans = accountClient.getNetworkVlans(mask='primaryRouter');

getVlanThing = {'locationId':265592,'packageId':174}
order = client['Product_Order'].placeOrder(productOrder)
pp.pprint(order);
