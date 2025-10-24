# Class file for machines representation
from enum import Enum
from network import NetworkConfiguration

class Machine:

    def __init__(self, name: str, os: str, networkConfigurations: list = None): 

        self.name = name
        self.os = os

class VirtualMachine(Machine):

    def __init__(self, name: str, os: str, cpu: int, ram: int, networkConfigurations: list = None):
        super.__init__(name, os, networkConfigurations)
        
        self.cpu = cpu
        self.ram = ram

class PhysicalMachine(Machine):

    def __init__(self, name: str, os: str, networkConfigurations: list = None):
        super.__init__(name, os, networkConfigurations)

        # Given network configurations will be needed to match the machine's amount of interfaces of each type.


