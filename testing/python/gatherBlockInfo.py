import SoftLayer
from SoftLayer import utils
import sys
import pprint
import logging as logger

apiUsername = ''
apiKey = ''
pp = pprint.PrettyPrinter(indent=4)

serverId = 7457068
client = SoftLayer.Client(username=apiUsername,api_key=apiKey)

# Gather the block devices
blockDevices = client['Virtual_Guest'].getBlockDevices(id=serverId,mask='mask[diskImage[metadataFlag]]')
pp.pprint(blockDevices)


# result = client['Virtual_Guest'].configureMetadataDisk(id=serverId)
# pp.pprint(result)

objectMask ="mask[id;note;transactionId;globalIdentifier;children.id;children.note;children.transactionId]"

# Gather the List of template device groups/images from softlayer as to reduce search
# preVGBDTGs = self.client['Account'].getPrivateBlockDeviceTemplateGroups(mask=objectMask)


# versionStamp = " [v"+version+"]"
# groupName = description + versionStamp
# if len(groupName) > 1000:
#         groupName = description[:1000-len(versionStamp)] + versionStamp

# Select disks to be captured
# disks = []
# for block_device in blockDevices:

#         if block_device['device'] != '1': # If not swap then add the disk to be captured
#                 logger.info("addding disk #%s to be captured" % block_device['device'])
#                 disks.append(block_device)

# disks = []
# disks.append(blockDevices[0])
# transactionInfo = client['Virtual_Guest'].createArchiveTransaction("TESTSETSET", disks, "SomethingHEre", id=serverId)
# pp.pprint(transactionInfo)
