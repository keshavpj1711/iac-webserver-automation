# Creating compute infrastr
import pulumi 
import pulumi_aws as aws
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from pulumi_aws.ec2 import tag


def create_sec_grp(vpc):
  """
    Creates a security group allowing HTTP (80) and SSH (22) access.
  """
  security_group = aws.ec2.SecurityGroup(
    "web-server-sg",
    name="example-security-group",
    description="Allow HTTP and SSH access",
    vpc_id=vpc.id,
    ingress=[
      # For SSH
      {
        "protocol": "tcp",
        "from_port": 22,
        "to_port": 22,
        "cidr_blocks": ["0.0.0.0/0"]
      },
      # For HTTP
      {
        "protocol": "tcp",
        "from_port": 80,
        "to_port": 80,
        "cidr_blocks": ["0.0.0.0/0"]
      }
    ],
    egress=[
      # For all outbound traffic
      {
        "protocol": "-1",
        "from_port": 0,
        "to_port": 0,
        "cidr_blocks": ["0.0.0.0/0"]
      }
    ],
    tags={
      "Name": "web-server-sec-grp"
    }
  )

  return security_group


def create_key_pair():
  """
    Creates an SSH key pair for secure access to EC2 instance.
    AWS generates both of them
  """

  private_key_path = "web-server-key"
  public_key_path = "web-server-key.pub"
  public_key_content: str

  # Check if public key present 
  if not (os.path.isfile(private_key_path) and os.path.isfile(public_key_path)):
    print("SSH key pair not found. Generating new key pair...")

    # Generate new ones with protocols followed by AWS
    try:
      # for private key
      private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
      )

      # for public key
      public_key = private_key.public_key()

      # Serialize private key in OpenSSH format
      private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.OpenSSH,
        encryption_algorithm=serialization.NoEncryption()
      )

      # serialization in public key in OpenSSH format
      public_ssh = public_key.public_bytes(
        encoding=serialization.Encoding.OpenSSH,
        format=serialization.PublicFormat.OpenSSH,
      )

      # Write private key
      with open(private_key_path, 'wb') as f:
        f.write(private_pem)
      os.chmod(private_key_path, 0o600)
      
      # Write public key
      with open(public_key_path, 'wb') as f:
        f.write(public_ssh)
      
      print(f"Generated new SSH key pair: {private_key_path} and {public_key_path}")

    except Exception as e:
      raise Exception(f"failed to generate SSH key pair: {e}")

    
  else:
    print(f"Using existing SSH key pair: {public_key_path}")

  # Read the public key from file
  try:
    with open(public_key_path, "r") as f:
      public_key_content = f.read().strip()
  except Exception as e:
    raise Exception(f"Error reading public key file: {e}")


  key_pair = aws.ec2.KeyPair(
    "web-server-key-pair",
    key_name="web-server-key",
    public_key=public_key_content,
    tags={
      "Name": "web-server-key-pair"
    }
  )

  return key_pair


def create_ec2_instance(subnet, sec_grp, key_pair): 
  """
    Create a t2.micro EC2 instance with Apache web server installed
    Subnet is req to place the instance in 
    Security group for firewall access
    Key pair for SSH access
  """

  user_script = ""  
  # Fetching data from bash script 
  try: 
    with open("user_script.sh", "r") as f:
      user_script = f.read()
  except FileNotFoundError:
    raise Exception(f"user_script.sh file not found. Please create the file")
  except Exception as e:
    raise Exception(f"Error reading user_script.sh: {e}")

  # Getting the latest Amazon Linux 2 AMI
  ami = aws.ec2.get_ami(
    most_recent=True,
    owners=["amazon"],  # ensures it's an official ami owned by amazon
    filters=[
      {
        "name": "name",
        "values": ["amzn2-ami-hvm-*-x86_64-gp2"]
        # hvm virtualization -> modern virtualization type
        # x86_64 -> 64 bit architecture
      }
    ]
  )

  # Creating EC2 instance
  instance = aws.ec2.Instance(
    "web-server-instance",
    instance_type="t2.micro",
    ami=ami.id,
    subnet_id=subnet.id,
    vpc_security_group_ids=[sec_grp.id],
    key_name=key_pair.key_name,
    user_data=user_script,
    tags={
      "Name": "web-server-instance"
    }
  )

  return instance



