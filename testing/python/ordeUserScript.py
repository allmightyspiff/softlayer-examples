import SoftLayer.API
 
#ENDPOINT = "http://stable.application.qadal0501.softlayer.local/v3/sldn/xmlrpc/"

#client = SoftLayer.Client(username=apiUsername,api_key=apiKey, endpoint_url = ENDPOINT)
client = SoftLayer.Client(username=apiUsername,api_key=apiKey)

#Order script for the gateway appliance:
print ("Package ID type - 174 - Network Gateway Appliance")
packageID = 174
#locationID = getDataCenterId(174)
print ("#############################################################")
locationID = "AMSTERDAM"
publicvlan = 494330#pub_vlans()
privatevlan = 494400#pri_vlans()
print ("")
print ("SL HA API to provision '1 pair of Vyatta' server.")
print ("")
hostname1 = "h1"#input("Enter the HA1 hostname: ")
domainname1 = "domain.test"#nput("Enter the HA1 domain name: ")
hostname2 = "h2"#input("Enter the HA2 hostname: ")
domainname2 = "domain.test"#input("Enter the HA2 domain name: ")
name = [{'hostname': hostname1, 'domain': domainname1, 'primaryNetworkComponent': {'networkVlan': {"id": publicvlan}}, 'primaryBackendNetworkComponent': {'networkVlan': {"id": privatevlan}}}, {'hostname': hostname2, 'domain': domainname2, 'primaryNetworkComponent': {'networkVlan': {"id": publicvlan}}, 'primaryBackendNetworkComponent': {'networkVlan': {"id": privatevlan}}}]
#hardware declaration without VLANs
#name2 = [{'hostname': hostname1, 'domain': domainname1}, {'hostname': hostname2, 'domain': domainname2 }]
print ("Placing Order Based on the inputs........ Server type: ", packageID,"In datacenter: ", locationID)
devcivyatta = [
                        {"id": 13738},
                        {"id": 21010},
                        {"id": 36044},
                        {"id": 876},
                        {"id": 1267},
                        {"id": 342},
                        {"id": 273},
                        {"id": 17129},
                        {"id": 55},
                        {"id": 58},
                        {"id": 420},
                        {"id": 418},
                        {"id": 21},
                        {"id": 57},
                        {"id": 906}
                    ]
orderData = {
"orderContainers" : [
{
"packageId" : packageID,
"location" : locationID,
"prices" : devcivyatta,
"quantity" : 2,
"hardware": name,
}
]
}
result = client['Product_Order'].verifyOrder(orderData)
#clustervyattaoverview(result)
#status = confirm()
#print (status)
print (result)
#if status == True:
#    print ("submitted the order")
#ordering = client['Product_Order'].placeOrder(orderData)
#print ordering
#else:
#    print ("Exiting Order on user cancellation" )
