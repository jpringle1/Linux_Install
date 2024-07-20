class ConfigOption:
    def __init__(self, json_object: dict) -> None:

        self.option = json_object["option"]
        self.value = json_object["value"]