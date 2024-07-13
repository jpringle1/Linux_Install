import json

class GitConfig:
    def __init__(self, filepath: str) -> None:
        jsonString = open(filepath)
        credentials = json.loads(jsonString)
        jsonString.close()
        self.email: str = credentials["email"]
        self.name: str = credentials["name"]