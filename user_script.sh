#!/bin/bash
yum update -y
yum install -y httpd # Apache web server package
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from IaC!</h1>" > /var/www/html/index.html
echo "<p>This web server was created using Pulumi and Python</p>" >> /var/www/html/index.html
echo "<p>Instance ID: $(curl -s http://169.254.169.254/latest/meta-data/instance-id)</p>" >> /var/www/html/index.html