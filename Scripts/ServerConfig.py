import json

from Models.ConfigOptions import ConfigOption
from Scripts import ConfigWriter

class ServerConfig:
    def __init__(
            self, 
            filepath: str) -> None:
        
        jsonString = open(filepath)
        config = json.loads(jsonString)
        jsonString.close()
        
        self.nasIpAddress: str = config["nasIpAddress"]
        self.credentialsDirectory: str = config["credentialsDirectory"]

    def setupSmbConfig(filepath):
        configOptions = ConfigOption(filepath)
        ConfigWriter.SetOptions(configOptions)