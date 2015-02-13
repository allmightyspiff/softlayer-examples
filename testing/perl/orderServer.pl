use lib "/Path/To/softlayer-api-perl-client/";
use SoftLayer::API::SOAP;
use Data::Dumper;
use strict;


my $api_username = 'USERNAME';
my $api_key = 'PASSWORD';

# Create a client to the SoftLayer_Virtual_Guest service.
my $client = SoftLayer::API::SOAP->new('SoftLayer_Virtual_Guest', undef, $api_username, $api_key);

my $myGuest = {
  hostname => 'myHostname',
  domain => 'testing.local',
  startCpus => 1,
  maxMemory => 1024,
  hourlyBillingFlag => 1,
  localDiskFlag => 1,
  datacenter => {
    name => "sjc01"
  }
};

# This is required to get SOAP to send the data formatted properly
bless($myGuest,'slapi:SoftLayer_Virtual_Guest');

my $orderRet = $client->createObject($myGuest);
if ($orderRet->fault) {
  print $orderRet->faultstring,"\n";
} else {
  print "Order submitted.\n";
}
