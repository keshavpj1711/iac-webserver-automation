# Internet Gateway

## What is Internet Gateway?

- Think of it as the main entrance/exit door for your VPC neighbourhood, without this your VPC is completely isolated from the internet.
- It's basically a component that **allows traffic to flow between your VPC and the Internet**

## Key Points

- Each VPC can have only one Internet Gateway

- AWS automatically makes it redundant and scalable
  - AWS manages the Internet Gateway infrastructure so you don't have to worry about it failing
  - It runs multiple Internet Fateways so that if one fails somehow, the traffic switches automatically
  - It's something AWS manages completely by itself and we don't see what's happening behind the scenes

- Performs **Network Address Translation (NAT)**
  - Automatically translates between private and public IP addresses
  - Your web server has a private IP **(like 10.0.1.15)** inside the VPC
  - Internet Gateway gives it a public IP **(like 54.123.45.67)** for internet access
  > Similar to what our router does for our home devices connected to it.

## Understanding Internet Gateways with Home Networks(Router/Modem)

### Your Home Setup:

- **Modem** = Connects your home network to the internet
- **Router** = Manages traffic within your home network
- **Devices** = Your computers, phones, etc.

### AWS Setup: 

- **Internet Gateway** = Like your modem (connects VPC to internet)
- **Route Tables** = Like your router (manages traffic flow)
- **EC2 Instances** = Like your devices

## Understanding what Internet Gateways don't do exactly

- Internet Gateway doesn't automatically gives internet access
- Instead they only provide connection point, we will still need: 
  - Route Tables, Public IPs, Security Groups etc.


