import pulumi 
import pulumi_aws as aws
from pulumi_aws.ec2 import route, route_table, tag 


def create_vpc(): 
  """
    Creates a VPC with DNS Support enabled and returns the VPC resource
  """
  vpc = aws.ec2.Vpc(
    "web-server-vpc",
    cidr_block="10.0.0.0/16",
    enable_dns_hostnames=True,  # allows this vpc to resolve domain names like google.com -> IP address
    enable_dns_support=True,  # allows to create DNS names for our resources
    tags={
      "Name": "web-server-vpc"
    })

  return vpc


def create_public_subnet(vpc):
  """
    Create a public subnet within the provided VPC 
  """
  public_subnet = aws.ec2.Subnet(
    "web-server-public-subnet",
    vpc_id=vpc.id,
    cidr_block="10.0.1.0/24",  # So we gave our VPC 10.0.0.0/16 and we are assigning the subnet 10.0.1.0/24 
    # that is IPs from 10.0.1.1 to 10.0.1.254
    availability_zone="us-east-1a",
    map_public_ip_on_launch=True,  # automatically assigns a public IP to any EC2 instance launched in this subnet
    tags={
      "Name": "web-server-public-subnet",
    }
  )

  return public_subnet


def create_internet_gateway(vpc):
  """
    Creates an Internet Gateway and attaches it to the provided VPC
  """
  internet_gateway = aws.ec2.InternetGateway(
    "web-server-igw",
    vpc_id=vpc.id,
    tags={
      "Name": "web-server-igw"
    }
  )

  return internet_gateway


def create_route_tables(vpc, igw):
  """
    Creates a route table with a route to the internet gateway
  """
  route_table = aws.ec2.RouteTable(
    "web-server-route-table",
    vpc_id=vpc.id,
    routes=[
      {
        "cidr_block": "0.0.0.0/0",  # this route is to match all internet traffic(anywhere on the internet)
        "gateway_id": igw.id,  # to know where to send the traffic to 
      }
    ],
    tags={
      "Name": "web-server-route-table"
    }
  )

  return route_table


def create_route_table_assc(subnet, route_table):
  """
    Associates a route table with a subnet 
  """
  association = aws.ec2.RouteTableAssociation(
    "web-server-rta",
    subnet_id=subnet.id,
    route_table_id=route_table.id,
  )

  return association