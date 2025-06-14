"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws.ec2 import route_table_association
from compute import create_key_pair, create_sec_grp
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

# Export the name of the resources
# This is basically to track what resources we have used in our pulumi stack
pulumi.export('vpc', vpc.id)
pulumi.export('subnet_id', public_subnet.id)
pulumi.export('internet_gateway_id', igw.id)
pulumi.export('route_table_id', route_table.id)
pulumi.export('route_table_assc_id', route_table_association.id)

