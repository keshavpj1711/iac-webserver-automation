# EC2 Instance

Our actual web server

# What is EC2 Instance?

- EC2 or Elastic Compute Cloud is AWS's virtual server service.
- An EC2 instance is like renting a computer in AWS's data center that you can control remotely.

## Types??

So these EC2 instances can have different computer configurations that we can rent.

### t2.micro instance

Specs: 
- 1vCPU
- 1GB RAM
- EBS storage: network attached disk storage
- Low to moderate network performance

### Why am i using t2.micro? 

- The first reason i am a student so basically at this point i am broke.
- Secondly this is the best things AWS has for learning about IaC.
  - Free tier eligible: well this is the only criteria that does the job for me

## Understanding User Data Scripts 

So when we create an EC2 Instance, we can provide a User Data Script that runs automatically when the server first starts.

A great example would be: 
```bash 
# For setting up Apache web server
yum update -y                    # Update all packages
yum install -y httpd             # Install Apache web server
systemctl start httpd            # Start Apache service
systemctl enable httpd           # Start Apache on boot
echo "<h1>Hello World!</h1><p>This is being served through a web-server that is made using pulumi fully automated and anyone can access it over the web since it's hosted on AWS</p>" > /var/www/html/index.html
```

### Why it's so great?

I mean we all can see how easy this made our job. 
Basically after running this we have our server up and running and serving our html file, and we didn't had to do any thing.