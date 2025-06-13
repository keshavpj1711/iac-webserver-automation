"""An AWS Python Pulumi program"""

import pulumi
from network import create_vpc, create_public_subnet


vpc = create_vpc()
public_subnet = create_public_subnet(vpc)

# Export the name of the resources
# This is basically to track what resources we have used in our pulumi stack
pulumi.export('vpc', vpc.id)
pulumi.export('subnet_id', public_subnet.id)

