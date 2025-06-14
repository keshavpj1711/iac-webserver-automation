# What is Infrastructure as Code? And why do we need this?

- Imagine you are a chef and you perfected this amazing recipe. 
- Now instead of making this recipe again and again manually(which may take forever and still be prone to errors), 
you write this exact recipe with all the precise little measurement. 
- Now anyone can follow your recipe and create the exact same delicious dish everytime.

IaC is exactly like this recipe, but instead for computer systems. 

- Instead of manually clicking buttons in AWS console or GCP console to create servers, networks and databases
  - which can be slow, error prone, impossible to remember 
- You write code for exactly what you want

> So basically the computer reads this script and builds the entire infrastructire perfectly every time.

# Why Python+Pulumi Instead of AWS Console?

## Why not click buttons in AWS to build your infrastructure?

The main issue is since building on the AWS console requires you to press multiple buttons to set different configs:
- It'll be very difficult to remember what config you created 
  - Even documenting the cofigs won't help, since when creating infrastructure again you will have to follow through somewhere
- Working with a team can be a huge mess as telling and making people understand can be quite daunting
- **Scalling**: Want' to scale your app, need 10 identical environments this can easily be done using IaC but using AWS console for that, it'll take up a huge amount of time.

## Why Pulumi instead of Terraform?

- The main reason is that to learn something like terraform i will have to give up some of my time.
- Not only that but my main reason for doing this project is getting a hands on experience on IaC. 
  - So once i get the basics of what we do, then Terraform would just be a language which can be learnt any time in the future.

### Features that comes along Pulumi

Mainly where pulumi shines is :

You can use **loops**, **functions**, **error handling** of python and all other **python libs** for better development.
- Examples: 
  - Want 5 similar servers you can use **loops**
  - **Conditionals**: If production use big server, if dev use small ones
  - **Functions**: Create reusable pieces of infrastructure 
  - Need csv to configure servers you can use pandas, this is how python libs can be useful


# Setting up AWS

So apps and programs that we build might use AWS directly and when they use their access is not managed by AWS web console it's managed using something known as IAM.

## What is IAM?

IAM is like security guard of AWS. It manages who can access what's in your AWS account. 
Even though you might be the owner, you'll still need to create proper creds for programmatic access.

## Why create a separate user instead of using root credentials?

- **Security**: If these credentials get compromised, you can delete just this user
- **Best Practice**: AWS strongly recommends never using root credentials for daily tasks, obviously!!
- **Granular Control:** You can give this user only the permissions it needs

## Creating a user in IAM Dashboard

Below are some of the things i encountered which i feel like should be kept in mind

### Setting Permission

For learning purposes we are going with simplest approach i.e:
- Choosing **Attach existing policies directly**
  - Since there are many options available to us: 
    - Adding user to a group(where this group has it's own set policies): This is a very solid option for handling multiple users
    - Copying permissions of an existing user 
- From Attach existing policy i chose: **AdministratorAccess** 
  - In order to not run into permission issues, since this project is supposed to be my first exp with this
  - **Do NOTE that in production it's better to use minimal permissions**


# Setting up Pulumi 

When we try to setup new pulumi project by:

```bash
pulumi new aws-python
```

- Pulumi needs to authenticate you with Pulumi Cloud to manage the infrastructure state.
- Think of Pulumi Cloud like a secure storage locker where Pulumi keeps track of what infrastructure you have created.

## Why does Pulumi need to know all this?
- **State Management**: Pulumi needs to remember what resources you've created
- **Team Collaboration**: Multiple people can work on the same infrastructure
- **Change Tracking**: See what changed between deployments
- **Free Service**: Pulumi Cloud's free tier is perfect for learning

## After login

- Basic info about project name and project description
- Asked about AWS region to deploy into, by default it was us-east-1
- A venv was created which i removed, since i was using conda

## After the command was done running

I had a ready to use Infrastructure as a code project.

### `__main.py__`

This where we will write our Python code that describes what AWS resources we want.

> In the begining it's auto configured to create a simple S3 bucket as an example

### `Pulumi.yaml`

Project Configuration: 
- basic info about your project 
  - like what prog lang you are using etc.

## Development Workflow to remember with pulumi

```bash
# 1. Write/modify Python code in __main__.py
# 2. Preview what will happen
pulumi preview

# 3. Deploy the changes
pulumi up

# 4. Check what was created
pulumi stack output

# 5. Clean up when done
pulumi destroy
```

# Buiding our Network Infrastructure for our web-server

So first we build all the components that make up our web-server that is:
- **VPC**: Virtual Private Cloud for our web-server to seperate it out from AWS and treat it as a network of it's own. 
  - In our case **CIDR: `10.0.0.0/16`** which means we have roughly ~65000 IPs in our hand
- **Subnet**: Defining subnets so that we can have a sub-network where our Web-server can live
  - Our public subnet is defined as `10.0.1.0/24`  
- **Internet Gateway**: This is where we will connect to the whole internet, it's like a gate where the internet meets our VPC.
- **Route Tables**: These are routes indicating where to direct the traffic to.
- **Route Table Association**: Without these route tables are useless as these are what connects these public subnet to the route tables.