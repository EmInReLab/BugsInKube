import abc
from src.Bugs import Bug

class KubernetesBug(Bug):
    def __init__(self, info:str, reproducable:bool=False)->None:
        Bug.__init__(self, "k8s", info, reproducable)
    
    def reproduce(self):
        if self.reproducable:
            # Reproduction functionality
            pass
        else:
            return