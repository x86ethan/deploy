# Class file for machines representation
from enum import Enum
from network import NetworkConfiguration

class Machine:

    def __init__(self, name: str, os: str, networkConfiguration: list): 

        self.name = name
        self.os = os

class VirtualMachine(Machine):

    def __init__(self, name: str, os: str, networkConfiguration: list, cpu: int, ram: int):
        super.__init__(name, os, networkConfiguration)
        
        self.cpu = cpu
        self.ram = ram

        