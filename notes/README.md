# Overview 

This is a place where I discuss what each of the things is, before getting my hands dirty with pulumi in python code.

## Real-world analogy to get a good idea of things:

- **VPC** = Your gated community
- **Subnets** = Different streets in your community
- **Internet Gateway** = The main entrance/exit to your community
- **Route Tables** = Street signs telling traffic where to go

## For incoming traffic(For people visiting your website the incoming traffic)

```text
Internet User → Internet Gateway → Route Table → Public Subnet → Security Group (checks port 80) → EC2 Instance (Apache serves webpage)
```

## For outgoing traffic(For downloading updates for server or you managing your server)

```text 
Your Computer (SSH client) → Internet Gateway → Route Table → Public Subnet → Security Group (checks port 22) → EC2 Instance (SSH server)
```

### What does it actually mean by sever downloading updates?

Since our web server is running on a amazon linux machine it needs to run updates for security patches and services.
- For example it might need to update the linux kernel or some security patches or Apache or Nginx
- For all this it would require some form of internet connectivity to update


# Table of Contents

## Network Infrastructure

- [VPC(Virtual Private Cloud)](./network_infra/VPC.md)
- [Subnets](./network_infra/Subnet.md)
- [Internet Gateways](./network_infra/InternetGateway.md)
- [Route Tables](./network_infra/RouteTables.md)

## Compute Resources

- [Security Groups](./compute_resources/SecurityGroups.md)
- [SSH Key pairs](./compute_resources/SSHKeyPairs.md)
- [EC2 Instance](./compute_resources/EC2Instance.md)


