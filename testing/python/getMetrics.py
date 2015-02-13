#
# Your SoftLayer API username and key.
#
# Generate an API key at the SoftLayer Customer Portal:
# https://manage.softlayer.com/Administrative/apiKeychain
import SoftLayer
import pprint


# the virtual guest ID you want to reload
virtualGuestId = 6058612

startDatetime = "2014-09-01T00:00:00-05:00"
endDatetime = "2014-09-02T10:37:00-05:00"


# Declare a new API service object
client = SoftLayer.Client(username=USERNAME,api_key=API_KEY)

try:
    # getting the metrics
    cpuMetrict = client['SoftLayer_Virtual_Guest'].getCpuMetricDataByDate(startDatetime, endDatetime, id=virtualGuestId)
    print (cpuMetrict)
    memoryMetrict = client['SoftLayer_Virtual_Guest'].getMemoryMetricDataByDate(startDatetime, endDatetime, id=virtualGuestId)
    print (memoryMetrict)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.            
    print("Unable to get metricts. "
          % (e.faultCode, e.faultString))
