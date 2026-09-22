def add_validation(i):
    if (len(i)== 4):
        pass
    else :
        print("Invalid address!!")
        return exit()
    return

def valid_range(i):
    if(0<=i and i<=255):
        pass
    else:
        print("Invalid address!!")
        return exit()
    return

ip = input("Enter an IPv4 address: ")
subnet_mask = input("Enter the subnet mask: ")

ip_parts = (ip.split('.'))
subnet_parts = subnet_mask.split('.')

add_validation(ip_parts)
add_validation(subnet_parts)

for i in range(4):
    ip_parts[i] = int(ip_parts[i])
    subnet_parts[i] = int(subnet_parts[i])

for i in range(4):
    valid_range(ip_parts[i])
    valid_range(subnet_parts[i])

block_size = 256 - int(subnet_parts[3])

block_number = (ip_parts[3]//block_size)*block_size

network_add = ip_parts.copy()
network_add[3] = block_number

broadcast_add = ip_parts.copy()
broadcast_add[3] = network_add[3]+block_size-1

first_host = network_add.copy()
first_host[3] = network_add[3]+1

last_host = broadcast_add.copy()
last_host[3] = broadcast_add[3]-1

usable_hosts = block_size-2

for i in range(4):
    network_add[i] = str(network_add[i])
    broadcast_add[i] = str(broadcast_add[i])
    first_host[i] = str(first_host[i])
    last_host[i] = str(last_host[i])

network_add = '.'.join(network_add)
broadcast_add = '.'.join(broadcast_add)
first_host = '.'.join(first_host)
last_host = '.'.join(last_host)

print()
print("Network Address:", network_add)
print("Broadcast Address:", broadcast_add)
print("First Host:", first_host)
print("Last Host:", last_host)
print("Usable Hosts:", usable_hosts)





