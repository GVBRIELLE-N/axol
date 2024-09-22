from axol_config.core import *

class axol:
    def __init__(self, name, element, hp, atk, dfn):
        self.name       = name
        self.element    = element
        self.hp         = hp
        self.atk        = atk
        self.defense    = dfn

    def __str__(self):
        return f"{self.name} | {self.hp} | Attack:{self.atk}, Defense: {self.defense}"
    
    def execute(self, command):
        print(f"{command} confirmed")