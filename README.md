# IPv4 Network Analyzer

A simple Python script that takes an IPv4 address and subnet mask and calculates the network address, broadcast address, usable host range, and total usable hosts.

Built as a mini project to practice IPv4 addressing, subnetting, and Python.

## Features

- Validates that the IP and subnet mask have exactly 4 octets, each within `0–255`
- Calculates:
  - Network Address
  - Broadcast Address
  - First / Last Usable Host
  - Number of Usable Hosts

## How It Works

1. Splits the entered IP and subnet mask into octets and validates them.
2. Calculates block size from the subnet mask's last octet.
3. Finds the network boundary the IP falls in.
4. Derives the broadcast address, host range, and usable host count from there.

> **Note:** Version 1 — only supports subnetting in the fourth octet (e.g. `/24`–`/30`). Doesn't yet support CIDR notation or masks spanning earlier octets (e.g. `/20`).

## Concepts Practiced

**Python:** functions, `input()`, string manipulation, `split()`/`join()`, lists, loops, conditionals, type conversion, input validation

**Networking:** IPv4 addressing, subnet masks, network/broadcast addresses, block size, usable hosts

## Usage

```bash
git clone https://github.com/Hemali78/ipv4-network-analyzer.git
cd ipv4-network-analyzer
python ipv4_analyzer.py
```

### Example

```
Enter an IPv4 address: 192.168.1.10
Enter the subnet mask: 255.255.255.0

Network Address: 192.168.1.0
Broadcast Address: 192.168.1.255
First Host: 192.168.1.1
Last Host: 192.168.1.254
Usable Hosts: 254
```

