# So we can talk to the SoftLayer API:
import SoftLayer.API
# For nice debug output:
from pprint import pprint as pp

api_username = ''
api_key = ''
client = SoftLayer.Client(
    username=api_username,
    api_key=api_key,
)


_filter = {
    'sshKeys': {
        'label': {
            'operation': '*= %s' % ('tokyo-')
        }
    }
}

_mask = "mask[id,label]"

sshkeys = client['Account'].getSshKeys(filter=_filter, mask=_mask)

pp(sshkeys)