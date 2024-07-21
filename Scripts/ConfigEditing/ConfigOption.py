from configparser import ConfigParser

class ConfigOption:
    def __init__(
            self, 
            filepath: str,
            section: str,
            option: str,
            value: str) -> None:
        
        self.filepath: str = filepath
        self.section: str = section
        self.option: str = option
        self.value: str = value

    def SetOption(self):
        config = ConfigParser()
        config.read(self.filepath)

        if not config.has_section(self.section):
            config.add_section(self.section)

        config.set(self.section, self.option, self.value)

        with open(self.filepath, "w") as configFile:
            config.write(configFile)