import SoftLayer

client = SoftLayer.Client()
test = client['Account'].getObject()
print ("TEST: ", test['id'])

name = [{'hostname': 'TEST1', 
         'domain': 'cgallo-test1', 
         'primaryNetworkComponent': 
            {'networkVlan': 
                {"id": 1165}
            }, 
            'primaryBackendNetworkComponent': 
            {'networkVlan': 
                {"id": 1164}
            }
        }, 
        {'hostname': 'TEST2', 
        'domain': 'cgallo-test2', 
        'primaryNetworkComponent': 
            {'networkVlan': 
                {"id": 1165}
            }, 
            'primaryBackendNetworkComponent': 
            {'networkVlan': 
                {"id": 1164}
            }
        }
    ]
orderData = {
    "orderContainers" : [
    {
        "packageId" : 46,
        "location" :352494,
        "quantity" : 2,
        "hardware": name,
    }
    ]
}
result = client['Product_Order'].verifyOrder(orderData)
print result
