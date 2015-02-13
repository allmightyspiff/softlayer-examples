
use lib "/Users/christopher/Code/softlayer-api-perl-client/";
use SoftLayer::API::SOAP;
use Data::Dumper;

my $client = SoftLayer::API::SOAP->new('SoftLayer_Account', undef, $api_username, $api_key); 
my $objectMask = { 'hardware' => {
    'remoteManagementAccounts' => {
      'username' => '',
      'password' => ''
    }
  }
};
my $test = $client->setOjectMask($objectMask);

print Dumper($test->fault);
my $hardware = $client->getHardware();

if ($hardware->fault) {
  die "getHostId had an error getting a hardware list:  " . $hardware->faultstring;
}

$hardware = $hardware->result;
# print Dumper($hardware);

my $i = 0;
while ($hardware->[$i]) {
  my $server = $hardware->[$i];
  my $temp = $server->{hostname};
  # print "HOSTNAME: " . $server->{hostname} . "  ";
  # print Dumper($server);
  # print "\n";
  # print "IP: " . $server->{networkManagementIpAddress} . "  ";
  # print "USERNAME: " . $server->{remoteManagementAccounts}->{username} . "  ";
  # print "PASS: " .  $server->{remoteManagementAccounts}->{password} . "  \n";
  $i++;
}
