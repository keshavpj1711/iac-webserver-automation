# VPC(Virtual Private Cloud)

## What is VPC?

VPC is like your own private neighbourhood in AWS. Just like our house is in a specific neighbourhood with it's own road, street addresses, and rules - VPC is also like a private network space in the cloud.

## Why do we need a VPC for a web server?

- **Isolation**: Your resources are seperated from other AWS costumers
  - The thing is even though we have seperate accounts, but still AWS runs on shared physical infrastructure 
    - Basically AWS has a massive data center with thousands of physical servers
    - Multiple customer's VM run on the same hardware

- **Control**: You decide the network rules and who can access what
- **Security**: You control traffic flow in and out of your network
- **Organization**: All your related resources live in the same "neighborhood"

## Real-world analogy to get a good idea of things:

- **VPC** = Your gated community
- **Subnets** = Different streets in your community
- **Internet Gateway** = The main entrance/exit to your community
- **Route Tables** = Street signs telling traffic where to go

## What does DNS support means?

DNS (Domain Name System) is like a phone book for the internet. When enabled in your VPC:

- Your servers can resolve domain names (like google.com) to IP addresses
- AWS can assign friendly names to your resources
  - This means that when we create different resources 
  - AWS automatically creates internal DNS names for these resources
- Essential for web servers that need to download updates or communicate with other services

### Without DNS support:
- Your web server only has an IP address: `10.0.1.15`
- You'd have to remember IP addresses for everything

### With DNS support:
- AWS automatically creates names like: `ip-10-0-1-15.ec2.internal`
- Your resources can find each other by name instead of IP
