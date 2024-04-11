import abc
import json
from src.utils.printPretty import *


class Bug:
    def __init__(self, platform:str, info:str, reproducable:bool=False)->None:
        self.platform = platform
        self.reproducable = reproducable
        self.info = info
    
    @abc.abstractmethod
    def reproduce(self):
        return
    
    def bugDefine(self):
        definition = self.info + "/definition.json"
        manifest = self.info + "/manifest.json"
        patch = self.info + "/patch.json"
        with open(definition, 'r') as file:
            definitionData = json.load(file)
        with open(manifest, 'r') as file:
            manifestData = json.load(file)
        with open(patch, 'r') as file:
            patchData = json.load(file)
        printDefinitionK8s(definitionData, manifestData, patchData)

        

    