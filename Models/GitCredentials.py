import json

class GitCredentials:
    def __init__(self, json_data: dict) -> None:
        json_object = json.loads(json_data)

        self.name: str = json_object["name"]
        self.email: str = json_object["email"]
        self.token: str = json_object["token"]