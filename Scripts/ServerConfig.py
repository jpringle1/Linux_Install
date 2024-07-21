import json

from Scripts.ConfigEditing.ConfigOptionCollection import ConfigOptionCollection

class ServerConfig:
    def __init__(self, json_data: dict) -> None:
        json_object = json.loads(json_data)
        
        self.nasIpAddress: str = json_object["nasIpAddress"]
        self.credentialsDirectory: str = json_object["credentialsDirectory"]

    def setupSmbConfig(json_data: dict):
        configOptions = ConfigOptionCollection(json_data)
        configOptions.SetOptions()