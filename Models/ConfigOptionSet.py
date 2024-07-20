from typing import List
from Models.ConfigOption import ConfigOption

class ConfigOptionSet:
    def __init__(self, json_object: dict) -> None:
        
        self.section: str = json_object["section"]
        self.options: List[ConfigOption] = json_object["options"]