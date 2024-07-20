import json
from typing import List

from Scripts.Enums.Repository import Repository

class RepositorySet:
    def __init__(self, json_data: dict) -> None:
        json_object = json.loads(json_data)

        self.repository: Repository = Repository(json_object["repository"])
        self.packages: List[str] = json_object["packages"]