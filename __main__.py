"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws.ec2 import route_table_association
from compute import create_ec2_instance, create_key_pair, create_sec_grp
from network import create_internet_gateway, create_route_table_assc, create_route_tables, create_vpc, create_public_subnet

# Create Network Infrasture
vpc = create_vpc()
public_subnet = create_public_subnet(vpc)
igw = create_internet_gateway(vpc)
route_table = create_route_tables(vpc, igw)
route_table_association = create_route_table_assc(public_subnet, route_table)

# Create Compute Infrastructure
sec_group = create_sec_grp(vpc)
key_pair = create_key_pair()
web_server = create_ec2_instance(public_subnet, sec_group, key_pair)

# Export network IDs
pulumi.export("vpc_id", vpc.id)
pulumi.export("subnet_id", public_subnet.id)
pulumi.export("internet_gateway_id", igw.id)
pulumi.export("route_table_id", route_table.id)

# Export compute IDs
pulumi.export("security_group_id", sec_group.id)
pulumi.export("key_pair_name", key_pair.key_name)

# Export web server information 
pulumi.export("instance_id", web_server.id)
pulumi.export("instance_type", "t2.micro")
pulumi.export("public_ip", web_server.public_ip)
pulumi.export("private_ip", web_server.private_ip)
pulumi.export("website_url", pulumi.Output.concat("http://", web_server.public_ip))
pulumi.export("ssh_command", pulumi.Output.concat("ssh -i web-server-key ec2-user@", web_server.public_ip))
pulumi.export("availability_zone", web_server.availability_zone)

# What these exports does is it makes anyone working on this get to know about the stack better
# So if you have better exports it'll be helpful 
# to the person who is just starting to work or 
# just want to know about the current state of the stack

# just a comment to test out github actions workflow