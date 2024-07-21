import json
from typing import List

from Models.ConfigOptionSet import ConfigOptionSet

class ConfigSectionSet:
    def __init__(self, json_data: dict) -> None:
        json_object = json.loads(json_data)
        
        self.filepath: str = json_object["filepath"]
        self.sections: List[ConfigOptionSet] = json_object["sections"]