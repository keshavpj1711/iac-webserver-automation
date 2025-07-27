#!/bin/bash
yum update -y
yum install -y httpd # Apache web server package
systemctl start httpd
systemctl enable httpd
# Ensure SSH is running
systemctl start sshd
systemctl enable sshd
echo "<h1>Hello from IaC!</h1>" > /var/www/html/index.html
echo "<p>This web server was created using Pulumi and Python</p>" >> /var/www/html/index.html
echo "<p>Instance ID: $(curl -s http://169.254.169.254/latest/meta-data/instance-id)</p>" >> /var/www/html/index.html
echo "<p>Visit this project's codebase at: <a href='https://github.com/keshavpj1711/iac-webserver-automation'>github link</a></p>" >> /var/www/html/index.html
echo "<p>Hope you are doing good.</p><p>-Keshav PJ</p>" >> /var/www/html/index.html