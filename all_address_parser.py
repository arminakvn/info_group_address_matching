def pars_street_name(full_address_string):
    from address import AddressParser, Address
    ap = AddressParser()
    address = ap.parse_address(full_address_string)
    return address.street
def pars_house_number(full_address_string):
    from address import AddressParser, Address
    ap = AddressParser()
    address = ap.parse_address(full_address_string)
    return address.house_number
def pars_zip(full_address_string):
    from address import AddressParser, Address
    ap = AddressParser()
    address = ap.parse_address(full_address_string)
    return address.zip
