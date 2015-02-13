## COMPLIANCE REPORT

import SoftLayer.API, socket
from pprint import pprint as pp


username = ''
key = ''
client = SoftLayer.Client(
    username= username,
    api_key = apiKey,
    )

#
# FORMAT TABLE                
#
class TablePrinter(object):
    "Print a list of dicts as a table"
    def __init__(self, fmt, sep=' ', ul=None):
        """        
        @param fmt: list of tuple(heading, key, width)
                        heading: str, column label
                        key: dictionary key to value to print
                        width: int, column width in chars
        @param sep: string, separation between columns
        @param ul: string, character to underline column label, or None for no underlining
        """
        super(TablePrinter,self).__init__()
        self.fmt   = str(sep).join('{lb}{0}:{1}{rb}'.format(key, width, lb='{', rb='}') for heading,key,width in fmt)
        self.head  = {key:heading for heading,key,width in fmt}
        self.ul    = {key:str(ul)*width for heading,key,width in fmt} if ul else None
        self.width = {key:width for heading,key,width in fmt}

    def row(self, data):
        return self.fmt.format(**{ k:str(data.get(k,''))[:w] for k,w in self.width.items() })

    def __call__(self, dataList):
        _r = self.row
        res = [_r(data) for data in dataList]
        res.insert(0, _r(self.head))
        if self.ul:
            res.insert(1, _r(self.ul))
        return '\n'.join(res)


#
# GET LIST OF ALL DEDICATED HARDWARE IN ACCOUNT
#

hardwarelist =client['Account'].getHardware()


for hardware in hardwarelist:

    hardwareid = hardware['id']

    #
    # LOOKUP HARDWARE INFORMATION BY HARDWARE ID
    #
    
    mask_object="datacenterName,serverRoom"
    hardware = client['Hardware'].getObject(mask=mask_object, id = hardwareid)

    print ("----------------------------------------------------------")
    print ("Hostname: %s (Public IP: %s  Private IP: %s  Mgmt IP: %s)" %(hardware['fullyQualifiedDomainName'],hardware['primaryIpAddress'], hardware['privateIpAddress'],hardware['networkManagementIpAddress']))
    print ("Datacenter: ",hardware['datacenterName'])
    rackname = client['Location'].getObject(mask="longName",id=hardware['serverRoom']['id'])
    print ("Location: ",rackname['longName'])
    print ("Serial Number: ",hardware['manufacturerSerialNumber'])
    print ()

    result = client['Hardware'].getComponents(id = hardwareid)

    #
    # BUILD TABLE
    #

    fmt = [
        ('Type   ',       'devicetype',        15),
        ('Manufacturer',  'manufacturer',      15),
        ('Name',          'name',              20),
        ('Description',   'description',       30),
        ('Modify Date',   'modifydate',        25),
        ('Serial Number', 'serialnumber',      15)
    ]

    #
    # POPULATE TABLE WITH COMPONENT DATA
    #
    data=[]
    for device in result:
        print (device)
        if device['hardwareComponentModel'].has_key('name'):
            hwdevice={}
            hwdevice['devicetype']=device['hardwareComponentModel']['hardwareGenericComponentModel']['hardwareComponentType']['type']
            hwdevice['manufacturer']=device['hardwareComponentModel']['manufacturer']
            hwdevice['name']=device['hardwareComponentModel']['name']
            hwdevice['description']=device['hardwareComponentModel']['hardwareGenericComponentModel']['description']
            hwdevice['modifydate']=device['modifyDate']
            if 'serialNumber' in device.keys(): hwdevice['serialnumber']=device['serialNumber']
            data.append(hwdevice)

    #
    # PRINT DATA TABLE
    #
    
    print( TablePrinter(fmt, ul='=')(data) )    
