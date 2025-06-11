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





