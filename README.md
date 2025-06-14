# 🚀 Infrastructure as Code Web Server
*Production-ready AWS infrastructure deployment using Pulumi & Python*

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pulumi](https://img.shields.io/badge/Pulumi-8A3391?style=for-the-badge&logo=pulumi&logoColor=white)
![AWS](https://img.shields.io/badge/Amazon_Web_Services-FF9900?style=for-the-badge&logo=amazonwebservices&logoColor=white)
![License](https://img.shields.io/badge/MIT-green?style=for-the-badge)

> Complete Infrastructure as Code implementation demonstrating cloud architecture, automation, and DevOps best practices using 100% AWS Free Tier resources.

## 🎯 Project Highlights

- **🆓 100% AWS Free Tier** - Zero cost infrastructure deployment
- **🏗️ Modular Python Architecture** - Clean, reusable, production-ready code
- **⚡ Complete Automation** - From VPC to running web server in one command
- **📚 Educational Documentation** - Comprehensive learning journey included
- **🔄 State Management** - Pulumi Cloud for team collaboration and change tracking

## 🛠️ Technical Skills Demonstrated

| Category | Technologies | Concepts Mastered |
|----------|-------------|-------------------|
| **Infrastructure as Code** | Pulumi, Python | Declarative infrastructure, State management |
| **Cloud Architecture** | AWS VPC, EC2, Security Groups | Network design, Security principles |
| **DevOps Practices** | Git, Modular code, Documentation | CI/CD readiness, Reproducibility |
| **Cost Management** | AWS Free Tier optimization | Resource monitoring, Budget control |

## 🏗️ Architecture Overview

```text 
Internet
   ↓
Internet Gateway (IGW)
   ↓
Route Table (0.0.0.0/0 → IGW)
   ↓
VPC (10.0.0.0/16)
   ↓
Public Subnet (10.0.1.0/24)
   ↓
Security Group (HTTP:80, SSH:22)
   ↓
EC2 Instance (t2.micro + Apache)
```

**Infrastructure Components:**
- **Custom VPC** with DNS support and public/private networking
- **t2.micro EC2 instance** with Apache web server (Free Tier eligible)
- **Security groups** with least-privilege access (HTTP:80, SSH:22)
- **Automated state management** via Pulumi Cloud
- **SSH key pair** for secure server access

## ⚡ Quick Start

### Prerequisites
- Python 3.8+ installed
- AWS account with Free Tier access
- Git installed
- Conda or Python virtual environment manager(optional)

### 1. Clone Repository

```bash
git clone https://github.com/keshavpj1711/iac-webserver-automation.git
cd iac-webserver-automation
```

### 2. Set Up Python Environment

```bash
# Using conda 
conda create -n infra-as-code python=3.10
conda activate infra-as-code

# Install dependencies
pip install -r requirements.txt
```

> Just in case you don't have conda installed or you prefer to make the venv using python directly
> then initialization of pulumi will do that for you in the future.


### 3. Configure AWS CLI

```bash
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Default region: us-east-1
# Default output format: json
```

### 4. Deploy Infrastructure

```bash
# Preview changes
pulumi preview

# If you are running this for the first time it will ask you to log in to your pulumi cloud which is totally free 
# During this it will login to your pulumi cloud
# Create a venv and install the required packages

# Deploy infrastructure
pulumi up
```

**Going with conda environment**

> One thing to keep in mind is if you are working with conda then initializing pulumi for the first time will create a venv in the folder\
> If you want to use your conda env you can edit the `Pulumi.yaml` to have this configuration

```yaml
runtime:
  name: python
  options:
    toolchain: pip
```

### 5. Access Your Web Server

```bash
# Get your web server URL
pulumi stack output website_url

# SSH into your server
pulumi stack output ssh_command
```


## 📁 Project Structure

```text
iac-webserver-automation
├── compute.py
├── journey.md
├── LICENSE
├── __main__.py
├── network.py
├── notes
│   ├── compute_resources
│   │   ├── EC2Instance.md
│   │   ├── SecurityGroups.md
│   │   └── SSHKeyPairs.md
│   ├── network_infra
│   │   ├── InternetGateway.md
│   │   ├── RouteTables.md
│   │   ├── Subnet.md
│   │   └── VPC.md
│   └── README.md
├── Pulumi.dev.yaml
├── Pulumi.yaml
├── README.md
├── requirements.txt
├── user_script.sh
```


## 🧠 Learning Journey

This project documents a complete Infrastructure as Code learning experience, covering:

**Core Concepts Mastered:**
- **Why IaC?** - Infrastructure as reproducible "recipes" vs manual clicking
- **Pulumi vs Terraform** - Real Python code with loops, functions, and error handling
- **AWS Networking** - VPC design, subnets, routing, and internet connectivity
- **Security** - SSH keys, security groups, and least-privilege access
- **State Management** - How Pulumi tracks and manages infrastructure changes

**Detailed Documentation:**
- 📖 **[Complete Journey](journey.md)** - Full learning experience with explanations
- 📝 **[Network Infrastructure Notes](notes/network_infra/)** - VPC, Subnets, IGW, Route Tables
- 💻 **[Compute Resources Notes](notes/compute_resources/)** - EC2, Security Groups, SSH Keys

## 🔧 Infrastructure Components

### Network Infrastructure
- **VPC**: Custom VPC with CIDR 10.0.0.0/16 (~65,000 IP addresses)
- **Public Subnet**: 10.0.1.0/24 in us-east-1a (~250 IP addresses)
- **Internet Gateway**: Enables internet connectivity for public resources
- **Route Table**: Routes traffic (0.0.0.0/0 → Internet Gateway)
- **Route Table Association**: Connects subnet to route table

### Compute Infrastructure
- **EC2 Instance**: t2.micro (1 vCPU, 1GB RAM) - Free Tier eligible
- **Security Group**: Allows HTTP (80) and SSH (22) with egress for updates
- **SSH Key Pair**: RSA 2048-bit keys for secure server access
- **User Data**: Automated Apache installation and configuration
- **AMI**: Latest Amazon Linux 2 with automatic security updates

## 💰 Cost Management

This project uses **only AWS Free Tier resources**:
- ✅ **t2.micro instance** (750 hours/month free)
- ✅ **VPC and networking** (always free)
- ✅ **Security groups** (always free)
- ✅ **30GB EBS storage** (free tier limit)
- ✅ **Pulumi Cloud** (free tier for personal use)

**Cost Prevention Measures:**
- Strictly t2.micro instances only
- No NAT Gateways (public subnets only)
- No Load Balancers (unless ALB in free tier)
- Automated cleanup with `pulumi destroy`

## 🎛️ Useful Commands

| Command | Purpose |
|---------|---------|
| `pulumi preview` | Preview infrastructure changes |
| `pulumi up` | Deploy infrastructure |
| `pulumi stack output` | Show deployment outputs |
| `pulumi stack output website_url` | Get web server URL |
| `pulumi stack output ssh_command` | Get SSH command |
| `pulumi destroy` | Remove all infrastructure |
| `pulumi stack history` | View deployment history |


## 🔄 State Management

**Pulumi automatically handles infrastructure state:**
- **Remote State Storage**: Pulumi Cloud (free tier)
- **Change Detection**: Only modifies what actually changed
- **Team Collaboration**: Multiple developers can work safely
- **History Tracking**: Complete audit trail of all changes
- **Rollback Capability**: Revert to previous infrastructure states


## 🚨 Troubleshooting

### Common Issues
| Issue | Solution |
|-------|----------|
| AWS credentials not configured | Run `aws configure` with your access keys |
| SSH key permissions error | Run `chmod 600 web-server-key` |
| Region mismatch | Use `us-east-1` for best Free Tier coverage |
| Pulumi login required | Run `pulumi login` and create free account |

### Validation Steps

1. Verify AWS credentials\
`aws sts get-caller-identity`

2. Test Pulumi configuration\
`pulumi preview`

3. Check web server\
`curl $(pulumi stack output public_ip)`

4. Verify SSH access\
`ssh -i web-server-key ec2-user@$(pulumi stack output public_ip)`


## 🧪 Reproducibility Test

Validate the complete Infrastructure as Code workflow:

1. Destroy everything: `pulumi destroy`

2. Confirm cleanup in AWS console

3. Redeploy from scratch: 
`pulumi up`



## 🎓 Key Learning Outcomes

- **Infrastructure as Code Principles** - Declarative, version-controlled infrastructure
- **AWS Cloud Architecture** - VPC design, security groups, and compute resources
- **Python for Infrastructure** - Real programming language benefits over DSLs
- **State Management** - How IaC tools track and manage infrastructure changes
- **Security Best Practices** - SSH keys, firewall rules, and least-privilege access
- **Cost Optimization** - Strategic use of AWS Free Tier resources
- **DevOps Workflows** - Preview, deploy, validate, and destroy patterns

## 🚀 Next Steps & Enhancements

- **Multi-Instance Setup** - Add Application Load Balancer with multiple t2.micro instances
- **Monitoring** - Integrate CloudWatch metrics and alarms (Free Tier)
- **CI/CD Pipeline** - GitHub Actions for automated testing and deployment
- **Multi-Environment** - Separate dev/staging/prod stacks

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Built with ❤️ keeping Infrastructure as Code principles in mind**

