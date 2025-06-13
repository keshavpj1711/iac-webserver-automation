# Subnet 

## What is Subnet?

- Building on our VPC 'neighbourhood' analogy, a subnet is like a specific street within your neighbourhood.
- Basically it's a smaller section of your VPC's network where you can actually place your resources(like webserver)

## Why do we need Subnet?

Think of it this way - you wouldn't put your house directly in the middle of a huge empty neighborhood. You'd want it on a specific street with proper addressing. Similarly:
- **VPC** = Your entire neighborhood (10.0.0.0/16 - can hold ~65,000 IP addresses)
  - To understand this better see in detail what subnet is.
- **Subnet** = A specific street (10.0.1.0/24 - can hold ~250 IP addresses)
- Your web server = Your house on that street (gets one specific IP like 10.0.1.15)

## Public vs Private Subnet

| **Property** | Public Subnet | Private Subnet |
|------|------|------|
| **Definition** | Can be directly accesed from the internet | Can't | 
| **Where is it used?** | When you want your resource to be accessible over the internet(in our case a webserver) | For Internal services like database or networks inside an oragnization |


## What makes a subnet public?

A subnet becomes public when it has a route to an Internet Gateway. Basically coninuing with our analogy 

- **Internet Gateway** = The main highway entrance to your neighborhood
- **Route Table** = Street signs pointing traffic toward the highway
- **Public Subnet** = A street with signs pointing to the highway

## Understanding the CIDR Blocks 



