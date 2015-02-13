import SoftLayer
from SoftLayer import utils
import sys
import pprint
import logging


pp = pprint.PrettyPrinter(indent=4)
client = SoftLayer.Client(username=apiUsername,api_key=apiKey)

domains = client['Account'].getDomains()

for domain in domains:
    records = client['Dns_Domain'].createARecord('test', '127.0.0.1', 86400, id=domain['id'])
    
