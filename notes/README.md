# Overview 

This is a place where I discuss what each of the things is, before getting my hands dirty with pulumi in python code.

## Real-world analogy to get a good idea of things:

- **VPC** = Your gated community
- **Subnets** = Different streets in your community
- **Internet Gateway** = The main entrance/exit to your community
- **Route Tables** = Street signs telling traffic where to go

## For incoming traffic(For people visiting your website)

```text
Internet User (Browser)
    ↓
Internet Gateway (main entrance to your VPC)
    ↓
Route Table (checks: "Where is 10.0.1.15?" → "That's local, go to subnet")
    ↓
Public Subnet (your street)
    ↓
Your Web Server (10.0.1.15)
```

## For outgoing traffic(For downloading updates for server)

```text 
Your Web Server (wants to reach update.amazon.com)
    ↓
Route Table (checks: "Where is update.amazon.com?" → "That's 0.0.0.0/0, go to IGW")
    ↓
Internet Gateway
    ↓
Internet (reaches Amazon's update servers)
```

### What does it actually mean by sever downloading updates?

Since our web server is running on a amazon linux machine it needs to run updates for security patches and services.
- For example it might need to update the linux kernel or some security patches or Apache or Nginx
- For all this it would require some form of internet connectivity to update


# Table of Contents

- [VPC(Virtual Private Cloud)](./VPC.md)
- [Subnets](./Subnet.md)
- [Internet Gateways](./InternetGateway.md)



