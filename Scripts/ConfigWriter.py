from configparser import ConfigParser
import json
from typing import List

class ConfigOption:
    def __init__(
            self, 
            filepath: str,
            section: str,
            option: str,
            value: str,
            description: str) -> None:
        
        self.filepath: str = filepath
        self.section: str = section
        self.option: str = option
        self.value: str = value
        self.description: str = description

    def SetOption(self):
        config = ConfigParser()
        config.read(self.filepath)

        if not config.has_section(self.section):
            config.add_section(self.section)

        config.set(self.section, self.option, self.value)

        with open(self.filepath, "w") as configFile:
            config.write(configFile)

class ConfigOptions:
    def __init__(
            self, 
            filepath: str) -> None:
        
        with open(filepath + ".json", 'r') as file:
            filestring = json.load(file)

        self.options: List[ConfigOption] = []

        for option in filestring:
            optionObj = ConfigOption(
                option["filepath"],
                option["section"],
                option["option"],
                option["value"],
                option["description"]
            )

            self.options.append(optionObj)

    def SetOptions(self):
        for option in self.options:
            option.SetOption()

