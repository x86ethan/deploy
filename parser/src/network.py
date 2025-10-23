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
        
    
        
    

# Abstract network configuration
class NetworkConfiguration:

    def __init__(self, interface_type: InterfaceType, externalPorts: list):

        self.interface_type
        
        # Si la configuration est statique
        self.ip
        self.mask
        self.gateway

        self.external_ports

class StaticConfiguration(NetworkConfiguration):

    def __init__(self, interface_type: InterfaceType, ip: str, gateway: str, ):
        super.__init__(interface_type)
        
        # IP adresses are written under 
        self.ip = ip
        self.gateway = gateway

# DHCP Configuration
class DHCPConfiguration(NetworkConfiguration):

    def __init__(self, interface_type, server: int):
        super.__init__(interface_type)

        self.dhcp_server = server