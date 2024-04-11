import abc
import json


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
        with open(definition, 'r') as definitionFile:
            definitionData = json.load(definitionFile)
        print(definitionData)

        

    