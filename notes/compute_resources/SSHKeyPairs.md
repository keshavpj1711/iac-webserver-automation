# SSH Key Pairs

These key pairs help us have a secure server access via SSH Protocol(Secure Shell Protocol).

## What are they and How do they work?

### The What Part

An SSH key pair is kinda like a special lock and key system for our server. As it's a pair it contains two components: 

- **Private Key**: Stays on our pc(like a house key)
- **Public Key**: Stays on our server(like our house lock)

### The How they work Part

- **Key Generation**: 
  - AWS creats a matched pair of keys
- **Public Key Deployment**: 
  - AWS puts the pubic key on our server
- **Private Key Download**: 
  - We download the key and keeps it safe

> During a connection via SSH your private key proves you own the matching public key.

