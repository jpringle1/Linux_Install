import json

class ConfigOptions:
    def __init__(self, filepath: str) -> None:
        jsonString = open(filepath + ".json")
        options = json.loads(jsonString)
        jsonString.close()
        self.filepath: str = options["filepath"]
        self.section: str = options["section"]
        self.option: str = options["option"]
        self.value: str = options["value"]
        self.description: str = options["description"]