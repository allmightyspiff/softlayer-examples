<?php
require_once '/Users/christopher/Code/sl-php/SoftLayer/SoapClient.class.php';

$apiUsername = '';
$apiKey = '';
$client = SoftLayer_SoapClient::getClient('SoftLayer_Virtual_Guest', null, $apiUsername, $apiKey);

$myGuest = new \stdClass();
$myGuest->hostname =  'ibm-test';
$myGuest->domain = 'ibm.com';
$myGuest->startCpus = 1;
$myGuest->maxMemory = 1024;
$myGuest->hourlyBillingFlag = 1;
$myGuest->localDiskFlag = 1;
$myGuest->blockDeviceTemplateGroup = new \stdClass();
$myGuest->blockDeviceTemplateGroup->globalIdentifier = 'f9db594e-c4c1-489d-870a-572bbd25f734';
$myGuest->datacenter = new \stdClass();
$myGuest->datacenter->name = "sjc01";


print "ORdering a server... " . print_r($myGuest,true) . "\n";

$result = $client->createObject($myGuest);
print "Result...\n" . print_r($result,true) . "\n";
print "REQUEST\n" . print_r($client->__getLastRequest(),true) . "\n";
print "REQUEST HEAD\n" . print_r($client->__getLastRequestHeaders(),true) . "\n";
