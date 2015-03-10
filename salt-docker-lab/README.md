# SoftLayer + SaltStack + Docker + Ghost Lab!

This lab is designed to take students through some of the basics of the SoftLayer API, by showing some practical examples of using SaltStack and Docker to deploy a Ghost blog.

## Prerequisites 
1. You will need a SoftLayer account.
  * Usually I create sub users on my account for this lab, and have the students use that. However if they have their own accounts already that can work as well. You will just need to have them create the Master server from the portal instead of from the create_users script.
2. If you want to create sub users, you will need a template user. This user will be used to clone new users from so that all the permissions are proper. I believe the default permissions should cover everything, but if you want to try locking them down, the following are required.
  1. Order Device
  2. Cancel Device
  3. View Virtual Server Details
  4. Manage SSH keys
  5. Manage DNS
3. The follow along document can be found here: http://sftlyr.com/dockerlab

## Setting up the lab for Sub Users
1. [lab_users.py](https://github.com/allmightyspiff/softlayer-examples/blob/master/salt-docker-lab/LabSetup/lab_users.py) will create the users and their master servers for you. You will need to make a few changes first
  1. Line 9: You should change the password to something you like
  2. Line 68: Change the domain to a domain you can add records to, otherwise step #8 will fail
  3. Line 71: Change to a Datacenter near you. 
  4. Line 98: Change to the ID for the template user you created
  5. Line 99-100: Change to your master user name and API key
  6. Line 117: Change the username prefix to something you like
2. Then just run the script
  ```bash
python lab_users.py --num-users=10
  ```
  That will create 10 users, and 10 master servers for them to login to.
3. Present the lab!
4. [cancel_users.py](https://github.com/allmightyspiff/softlayer-examples/blob/master/salt-docker-lab/LabSetup/cancel_users.py) will clean the lab up for you, but you will need to make some changes. 
  1. Line 55-56: Your API username + key
5. Run the cancel script, change the prefix to whatever you used to create the users
```bash
python cancel_users --prefix=devat
```

## Using personal accounts
If the students are using their own accounts, they will need to create a new server based off a public image. 

1. Login to https://control.softlayer.com
2. Navigate to Devices -> Manage -> [Images](https://control.softlayer.com/devices/images)
3. Make sure you are looking at the PUBLIC images (its a drop down above the image list)
4. Search for a Template name of salt (there are a lot of images)
  * Specifically [SoftLayer-SaltStack-Docker-Ghost Lab Master](https://control.softlayer.com/devices/images/450151?imageType=public)
5. Use the "Action" button to order a new Hourly Virtual Server
6. Present the lab!



