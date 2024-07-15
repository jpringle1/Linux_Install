import json
import os

class Configuration:
    def __init__(self) -> None:
        self.gitConfig = self.parse("/Resources/gitConfig.json"),
        self.serverConfig = self.parse("/Resources/serverConfig.json"),
        self.smbConfig = self.parse("/Resources/smbConfig.json"),
        self.drives = self.parse("/Resources/drives.json"),
        self.packages = self.parse("/Resources/packages.json"),
        self.symLinks = self.parse("/Resources/symLinks.json"),
        self.configOptions = self.parse("/Resources/configOptions.json"),
        self.grubOptions = self.parse("/Resources/grubOptions.json"),
        self.gitToken = self.parse("/.env/.gittoken")

    def parse(file_path):
        with open(os.getcwd() + file_path, 'r') as file:
            return json.load(file)