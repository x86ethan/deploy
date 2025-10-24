from parser.network import validateIP, validatePort

def test_validate_ip_valid():
    """Tests a valid CIDR IP address."""
    assert validateIP("192.168.1.2/32") is True

def test_validate_ip_invalid_mask_too_high():
    """Tests a CIDR with a mask greater than 32."""
    assert validateIP("192.168.1.2/33") is False

def test_validate_ip_invalid_mask_too_low():
    """Tests a CIDR with a mask less than 0."""
    assert validateIP("0.0.0.0/-1") is False

def test_validate_ip_invalid_octet_too_high():
    """Tests an IP with an octet greater than 255."""
    assert validateIP("256.0.0.0/32") is False

def test_validate_ip_invalid_octet_negative():
    """Tests an IP with a negative octet."""
    assert validateIP("-1.0.0.0/32") is False

def test_validate_ip_missing_mask():
    """Tests an IP address string without a CIDR mask."""
    assert validateIP("0.0.0.0") is False

def test_validate_ip_too_few_octets():
    """Tests an IP with less than 4 octets."""
    assert validateIP("0.0.0/32") is False

def test_validate_ip_too_many_octets():
    """Tests an IP with more than 4 octets."""
    assert validateIP("0.0.0.0.0/32") is False

def test_validate_negative_port():
    """Tests a negative port number."""
    assert validatePort(-1) is False

def test_validate_port_too_high():
    """Tests a port number greater than 65535."""
    assert validatePort(65536) is False

def test_validate_port_valid():
    """Tests a valid port number."""
    assert validatePort(80) is True