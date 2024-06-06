def ip_to_binary(ip):
    return '.'.join(f'{int(octet):08b}' for octet in ip.split('.'))

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: python ip_to_binary_converter.py <ip_address>')
        sys.exit(1)

    ip_address = sys.argv[1]
    try:
        binary_ip = ip_to_binary(ip_address)
        print(binary_ip)

    except ValueError:
        print("Invalid IP address format. Please enter a valid IP address.")