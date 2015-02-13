<?php

require_once ('/Users/christopher/Code/softlayer-object-storage-php/lib/ObjectStorage/Util.php');


 # Configuring the object storage
 $options = array('adapter' => ObjectStorage_Http_Client::SOCKET, 'timeout' => 10);
 $host = 'https://dal05.objectstorage.softlayer.net'; // the SoftLayer Object Storage API host
 $username = 'ACCOUNT:USERNAME'; // user name and password is display at  						
 $password = '';
 $objectStorage = new ObjectStorage($host, $username, $password, $options);
 # the name of your container, this container will be used to add a new file
 $containerName = 'newVideos';

try{

$container = $objectStorage->with($containerName)->get();
$cdnUrls = $container->getCdnUrls();
// print_r($container);
print_r($cdnUrls);
foreach ($cdnUrls as $cdnUrl) {
	print_r($cdnUrls);
}
}catch(Exception $e){

die( $e->getMessage());
}

        
?>
