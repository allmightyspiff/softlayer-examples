<?php
require_once '/Users/christopher/Code/sl-php/SoftLayer/XmlrpcClient.class.php';


$apiUsername = '';
$apiKey = '';

$client = SoftLayer_XmlrpcClient::getClient('SoftLayer_Product_Order', null, $apiUsername, $apiKey);


$price1 = new \stdClass();
$price1->id = 1641;

$guest = new \stdClass();
$guest->id = 7444860;

$priceClient = SoftLayer_XmlrpcClient::getClient('SoftLayer_Product_Package', 46, $apiUsername, $apiKey);
$objectMask = new SoftLayer_ObjectMask();
$objectMask->description;
$objectMask->capacity;
$objectMask->prices->id;
$objectMask->categories->id;

$priceClient->setObjectMask($objectMask);
$items = $priceClient->getObject();
// print_r($i tems);


// prices = items.map do |item|
//   if (item['categories'].detect {|c| c['id'] == 80} and item['capacity'] == cores.to_s and item['description'] !~ /^Private/) or
//      (item['categories'].detect {|c| c['id'] == 3} and item['capacity'] == mem.to_s)
//     item['prices'].first
//   end
// end.compact



$upgrade = new \stdClass();
$upgrade->complexType = "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade";
$upgrade->prices = array($price1);
$upgrade->properties = new \stdClass();
$upgrade->properties->maintenanceWindow;
$upgrade->properties->maintenanceWindow->name = "MAINTENANCE_WINDOW";
$upgrade->properties->maintenanceWindow->value = "now";
$upgrade->virtualGuests = array($guest);
print_r($upgrade);


$response = $client->verifyOrder($upgrade);

print_r($response);
