# Class file for network configurations
from enum import Enum

InterfaceType = Enum("InterfaceType", ["wireless", "wired"])

def validateIP(ip: str):

    # IP adresses are written under CIDR format 
    try:
        add = ip.split("/")[0].split(".")
        mask = ip.split("/")[1]
    except IndexError:
        # The adress is not under CIDR format
        return False

    if len(add) != 4:
        # This is not IPv4 format 
        return False

    for n in add:
        try:
            if int(n) > 255 or int(n) < 0:
                # A litteral in the adress exceeds 255 or is below 0
                return False
        except ValueError:
            # A litteral in the adress is not a number
            return False
        
    try:
        if int(mask) > 32 or int(mask) < 0:
            # The mask exceeds 32 or is below 0
            return False
    except ValueError:
        # The mask is not a number 
        return False
    
    return True
        
def validatePort(port: int):

    try:
        p = int(port)
        if p >= 0 and p <= 65535:
            return True
        else:
            return False
    except ValueError:
        return False
        
    

# Abstract network configuration
class NetworkConfiguration:

    def __init__(self, interfaceType: InterfaceType, externalPorts: list = None):
        self.interface_type = interfaceType
        self.external_ports = externalPorts 

class StaticConfiguration(NetworkConfiguration):

    def __init__(self, interface_type: InterfaceType, ip: str, gateway: str):
        super.__init__(interface_type)
        
        if validateIP(ip):
            self.ip = ip
        else:
            raise ValueError("Given IP is not correct. Must be under a valid CIDR format")
    
        if validateIP(gateway):
            self.gateway = gateway
        else: 
            raise ValueError("Given gateway is not correct. Must be under a valid CIDR format")
    

# DHCP Configuration
class DHCPConfiguration(NetworkConfiguration):

    def __init__(self, interfaceType: InterfaceType, server: int, externalPorts: list = None):
        super.__init__(interfaceType, externalPorts)

        if validateIP(server):
            self.server = server