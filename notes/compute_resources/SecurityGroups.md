# Security Groups

It's basically our web server's firewall

## What is it?

Think of it as a virtual firewall that sits directly in front of your web server. It's like having a security guard who checks everyone through the network traffic entering our VPC.

## Usecase

Without this: 
- your web-server would be completely exposed to the internet
- anyone could try to connect on any port

With this: 
- only specific types of traffic are allowed
- you control who can access what

## Ingress Rules(Inbound Traffic)

- Port 22 (SSH): For server management and troubleshooting, basically you accessing it over internet for updates or security patches
- Port 80 (HTTP): For web traffic from browsers, basically for people accessing it

## Egress Rules(Outbound Traffic)

```python 
{
    "protocol": "-1",
    "from_port": 0,
    "to_port": 0,
    "cidr_blocks": ["0.0.0.0/0"]
}
```

- Protocol `-1`: All protocols (TCP, UDP, ICMP, etc.)
- Port 0: All ports
- Result: Your server can connect to anywhere on the internet

### Why need for an outbound access

- **Install sofware updates and softwares**(like Apache, PHP etc)
- **API Calls**
- **Time sync**