import json

class ServerConfig:
    def __init__(self, filepath: str) -> None:
        jsonString = open(filepath)
        config = json.loads(jsonString)
        jsonString.close()
        self.smbUsername: str = config["smbUsername"]
        self.smbPassword: str = config["smbPassword"]
        self.smbDomain: str = config["smbDomain"]
        self.nasIpAddress: str = config["nasIpAddress"]
        self.credentialsDirectory: str = config["credentialsDirectory"]