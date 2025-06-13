# Overview 

This is a place where I discuss what each of the things is, before getting my hands dirty with pulumi in python code.

## For incoming traffic(For people visiting your website)

> **Internet** → **Internet Gateway** → **Route Table** → **Public Subnet** → **Web Server**

## For outgoing traffic(For downloading updates for server)

> **Your Web Server** → **Public Subnet** → **Route Table** → **Internet Gateway** → **Internet**

### What does it actually mean by sever downloading updates?

Since our web server is running on a amazon linux machine it needs to run updates for security patches and services.
- For example it might need to update the linux kernel or some security patches or Apache or Nginx
- For all this it would require some form of internet connectivity to update


# Table of Contents

- [VPC(Virtual Private Cloud)](./VPC.md)
- [Subnets](./Subnet.md)
- [Internet Gateways](./InternetGateway.md)



