# So we can talk to the SoftLayer API:
import SoftLayer.API
from SoftLayer.managers import monitor as monitor
# For nice debug output:
from pprint import pprint as pp
from datetime import datetime, timedelta, tzinfo

client = SoftLayer.Client(
    username=api_username,
    api_key=api_key,
)

manager = monitor.MonitoringManager(client, 'Virtual_Guest')
manager2 = monitor.MonitoringManager(client, 'Hardware_Server')


print "\033[31mFirst\033[0m"
# output = manager.get_status(6486684)


print "\033[31mSecond\033[0m"
# output = manager.get_status(6674100)


print "\033[31mThird\033[0m"
# output = manager2.get_status(285370)

output = manager.list_hardware_status()
pp(output)


