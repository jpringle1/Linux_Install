import json
import os

class Configuration:
    def __init__(
            self,
            configName: str,
            parent = "Resources",
            extension = "json") -> None:
        
        return self.parse("/" + parent + "/" + configName + "." + extension)
        
    def parse(file_path):
        with open(os.getcwd() + file_path, 'r') as file:
            return json.load(file)