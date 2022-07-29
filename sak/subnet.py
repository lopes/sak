from ipaddress import ip_address, ip_network

def ip_info(addr):
    address = ip_address(addr.split('/')[0])
    network = ip_network(addr, False)
    print(f'''
Address............: {address}
Mask...............: {network.netmask}
Wildcard...........: {network.hostmask}
Wildcard...........: {network.hostmask}
Network Address....: {network.network_address}
Broadcast Address..: {network.broadcast_address}
Number of Addresses: {network.num_addresses}
    ''')
