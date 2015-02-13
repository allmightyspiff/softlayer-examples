<?php
require_once '/Users/christopher/Code/sl-php/SoftLayer/SoapClient.class.php';
date_default_timezone_set('America/Los_Angeles');

// require_once dirname(__FILE__) . '/SoftLayer/SoapClient.class.php';



$apiUsername = 'USERNAME';
$apiKey  = '';


$startDate = new DateTime('2014-11-01T00:00:00-06:00');
$endDate = new DateTime('2014-12-01T00:00:00-06:00');

//The First Object Mask. Used to get all the front line brands, which will have the
//accounts that are actually buying things
$objectMask = new SoftLayer_ObjectMask();
$objectMask->ownedBrands->allOwnedAccounts->ownedBrands;

//Mask for the front line brands, used to get all their accounts, and their invoices
$brandMask = new SoftLayer_ObjectMask();
$brandMask->allOwnedAccounts->invoices;

//Used to get all the actual line items from an invoice
$invoiceMask = new SoftLayer_ObjectMask();
$invoiceMask->items;
$invoiceMask->invoiceTotalAmount;


//This filters out all invoices that are not in our date range.
//all based on the invoices createDate
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

$client = SoftLayer_SoapClient::getClient('SoftLayer_Account', null, $apiUsername, $apiKey);
$client->setObjectMask($objectMask);

$response = $client->getObject();


// print_r($response);


//Start off with the main brand
foreach ($response->ownedBrands as $brand) {
    print "BRAND=\e[31m" . $brand->keyName .  " ::" . $brand->id . "\e[0m=\n";

    //Go into each of the top brands accounts
    foreach ($brand->allOwnedAccounts as $account) {
        print "==\e[32m" . $account->companyName ."\e[0m\n";

        //Go into each of those's accounts brands...
        foreach ($account->ownedBrands as $brand1) {
            print "====\e[33m" . $brand1->name ." ::" . $brand1->id . "\e[0m\n";

            //From that brand, get all the brand's owned accounts, with their invocies from the current month
            $brandClient = SoftLayer_SoapClient::getClient('SoftLayer_Brand', $brand1->id, $apiUsername, $apiKey);
            $brandClient->setObjectMask($brandMask);
            $brandClient->setObjectFilter($filter);

            $brandInvoice = $brandClient->getAllOwnedAccounts();

            //Go through each of the accounts on the brand
            foreach ($brandInvoice as $brandAccount) {

                //This is recursive and we don't need it.
                unset($brandAccount->brand);
                print "=====\e[94m" . $brandAccount->companyName ." ::" . $brandAccount->id . "\e[0m\n";

                //Go through each of the accounts monthly invoices
                foreach ($brandAccount->invoices as $invoice) {
                    print "Created: " . $invoice->createDate . " TYPE: " . $invoice->typeCode ."  Invoice ID: " . $invoice->id . "\n";

                    //Here we get the actual invoice and all the billing items inside of it
                    $bClient = SoftLayer_SoapClient::getClient('SoftLayer_Billing_Invoice', $invoice->id , $apiUsername, $apiKey);
                    $bClient->setObjectMask($invoiceMask);
                    $bt = $bClient->getObject();
                    print "====\e[42;90m" . $bt->invoiceTotalAmount ."\e[0m\n";

                    //Go through each item on the invoice and print out its decription + fee.
                    //There are a few other fields that could be billable, but these are the main ones.
                    foreach ($bt->items as $lineItem) {
                        unset($lineItem->invoice);
                        $fee = $lineItem->recurringAfterTaxAmount + $lineItem->oneTimeAfterTaxAmount;
                        print "====\e[35m" . $lineItem->description . " => " . $fee . "$ \e[0m\n";
                    }

                }//end invoice

            } // end brand->allOwnedAccounts->brand->allOwnedAccounts
        } //end brand->allOwnedAccounts->Brand
    } // end brand->allOwnedAccounts
} // end brand

//Done
