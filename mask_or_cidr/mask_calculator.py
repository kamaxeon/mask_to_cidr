import ipaddress


def invert_mask(mask_or_cidr):
    try:
        ip = ipaddress.IPv4Network(f'10.0.0.1/{mask_or_cidr}', strict=False)
        if '.' in mask_or_cidr:
            return str(ip.prefixlen)
        else:
            return str(ip.netmask)
    except ipaddress.NetmaskValueError:
        return 'invalid'
