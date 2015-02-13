<?php


require_once '/Users/christopher/Code/sl-php/SoftLayer/SoapClient.class.php';

$startDate = new DateTime('2014-11-01T00:00:00-06:00');
$endDate = new DateTime('2014-12-01T00:00:00-06:00');

$brandClient = SoftLayer_SoapClient::getClient('SoftLayer_Brand', 27322, $apiUsername, $apiKey);

$brandMask = new SoftLayer_ObjectMask();
$brandMask->allOwnedAccounts->invoices;





$filter = new stdClass();
$filter->allOwnedAccounts = new stdClass();
$filter->allOwnedAccounts->invoices = new stdClass();
$filter->allOwnedAccounts->invoices->createDate = new stdClass();
$filter->allOwnedAccounts->invoices->createDate->operation = 'betweenDate';
$filter->allOwnedAccounts->invoices->createDate->options = array();
$filter->allOwnedAccounts->invoices->createDate->options[0] = new stdClass();
$filter->allOwnedAccounts->invoices->createDate->options[0]->name = 'startDate';
$filter->allOwnedAccounts->invoices->createDate->options[0]->value = array($startDate->format('m/d/Y H:i:s'));
$filter->allOwnedAccounts->invoices->createDate->options[1] = new stdClass();
$filter->allOwnedAccounts->invoices->createDate->options[1]->name = 'endDate';
$filter->allOwnedAccounts->invoices->createDate->options[1]->value = array($endDate->format('m/d/Y H:i:s'));



$brandClient->setObjectMask($brandMask);
$brandClient->setObjectFilter($filter);

$brandInvoice = $brandClient->getAllOwnedAccounts();

print_r($brandInvoice);
