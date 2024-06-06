def ip_identify(ip):
    octets = ip.split('.')
    if len(octets) != 4:
        raise ValueError("Invalid IP address format. Please enter a valid IP address.")
    
    for octet in octets:
        if not octet.isdigit():
            raise ValueError("Invalid IP address format. Please enter a valid IP address.")
        if int(octet) < 0 or int(octet) > 255:
            raise ValueError("Invalid IP address format. Please enter a valid IP address.")
    
    first_octet = int(octets[0])
    
    if first_octet >= 1 and first_octet <= 126:
        return 'Class A'
    elif first_octet >= 128 and first_octet <= 191:
        return 'Class B'
    elif first_octet >= 192 and first_octet <= 223:
        return 'Class C'
    elif first_octet >= 224 and first_octet <= 239:
        return 'Class D'
    elif first_octet >= 240 and first_octet <= 255:
        return 'Class E'
    else:
        return 'Invalid IP address'
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: python identify_ip_class.py <ip_address>')
        sys.exit(1)

    ip_address = sys.argv[1]
    try:
        ip_class = ip_identify(ip_address)
        print(ip_class)
    except ValueError as e:
        print(e)
