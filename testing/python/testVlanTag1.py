import SoftLayer
import pprint
pp = pprint.PrettyPrinter(indent=2)

#comma seperated list of ids
serverIds = [153015] 

#comma seperated list of public vlan nubmers to tag on each server
publicVlanNumbers = [1125,1110]
#comma seperated list of private vlan nubmers to tag on each server
privateVlanNumbers = [939,803]



def addVlanTrunks(id, vlans):
    for vlanNumber in vlans:
        print "Adding vlan %s to %s" % (vlanNumber,id)
        result = client['Network_Component'].addNetworkVlanTrunks([{'vlanNumber':vlanNumber}],id=id)
        vlan = client['Network_Component'].getNetworkVlanTrunks(id=id)
        pp.pprint(result)
        pp.pprint(vlan)


client = SoftLayer.Client(username=apiUsername,api_key=apiKey)

mgr = SoftLayer.HardwareManager(client)
nmgr = SoftLayer.NetworkManager(client)

for sid in serverIds:
    hardware = mgr.get_hardware(sid)
    privateIP = hardware['primaryBackendIpAddress']
    print "Private IP is: %s" % (privateIP) 
    publicIP = hardware['primaryIpAddress']
    print "Public IP is: %s" % (publicIP)

    for component in hardware['networkComponents']:
        try:
            if (component['primaryIpAddress'] == publicIP):
                addVlanTrunks(component['id'],publicVlanNumbers)
            elif (component['primaryIpAddress'] == privateIP):
                addVlanTrunks(component['id'],privateVlanNumbers)
            # result = client['Network_Component'].clearNetworkVlanTrunks(id=component['id'])
            mask = 'networkVlan, networkVlanTrunks, uplinkComponent[networkVlanTrunks]'
            nic = client['Network_Component'].getObject(id=component['id'], mask=mask)
            pp.pprint(nic)
        except KeyError:
            continue

    print "Done with %s " % (hardware['hostname'])
    print "====================================="


