# Class file for network configurations
from enum import Enum

InterfaceType = Enum("InterfaceType", ["wireless", "wired"])


        
    

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