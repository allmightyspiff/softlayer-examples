# So we can talk to the SoftLayer API:
import SoftLayer.API
from SoftLayer import VSManager
# For nice debug output:
from pprint import pprint as pp


client = SoftLayer.Client(
    username=api_username,
    api_key=api_key,
)

config = {'imageTemplateId': 119634, 'sshKeyIds': [87634, 96794, 96788]}
output = client['Hardware_Server'].reloadOperatingSystem('FORCE', config, id=87341)

pp(config)
print "RESULT\n"
pp(output)
