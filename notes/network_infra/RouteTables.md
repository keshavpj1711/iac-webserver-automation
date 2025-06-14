# Route Tables 

## What is Route Table?

- Think of a Route Table as the GPS navigation system for your VPC.
- A Route Table tells network traffic which path to take to reach its destination.

Basically it's a set of rules(called routes) that determines where network traffic goes within your VPC and to the internet.

## Essential Routes for Web Server

### Route 1: Local traffic(Automatic)

```text
Destination: 10.0.0.0/16
Target: local
```
If traffic is going to any IP address within your VPC (10.0.0.0/16), keep it local - don't send it anywhere else.

### Route 2: Internet traffic(to be configured)

```text
Destination: 0.0.0.0/0  
Target: igw-12345 (your Internet Gateway)
```
If traffic is going anywhere else on the internet (0.0.0.0/0 means 'everywhere'), send it to the Internet Gateway

### Why `0.0.0.0/0` Means "The Internet"

`0.0.0.0/0` is like saying "everywhere else" or "the default route":

- `0.0.0.0` = Starting IP address (the very first IP)
- `/0` = Include ALL possible IP addresses
- Result: Every IP address on the internet

## Route Table Association

Creating a route table isn't enough - you must associate it with your subnet:\
**Without Association:** Route Table exists but doesn't control any traffic



