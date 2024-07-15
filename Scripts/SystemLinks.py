import json
import os
from typing import List

class SymLink:
    def __init__(
            self, 
            sourceName: str, 
            destinationName: str, 
            sourcePath: str, 
            destinationPath: str) -> None:
        
        self.sourceName = sourceName
        self.destinationName = destinationName
        self.sourcePath = sourcePath
        self.destinationPath = destinationPath

    def __repr__(self) -> str:
        return f"SymLink(sourceName={self.sourceName}, destinationName={self.destinationName}, sourcePath={self.sourcePath}, destinationPath={self.destinationPath})"

    def addSymlink(self):
        if os.path.isfile(self.destinationPath):
            os.remove(self.destinationPath)

        commandExecution = os.popen(f'sudo ln -s {self.destinationPath} {self.sourcePath}')
        print(commandExecution.read())
        print(commandExecution.close())

class SymLinks:
    def __init__(self, filepath: str) -> None:
        with open(filepath, 'r') as file:
            file = json.load(file + ".json")
        
        self.symLinks: List[SymLink] = []
        
        for entry in file:
            sourceDir = entry["sourceDirectory"]
            destinationDir = entry["destinationDirectory"]
            for link in entry:
                symLinkObj = SymLink(
                    link["sourceName"],
                    link["destinationName"],
                    sourceDir, 
                    destinationDir
                )
                self.symLinks.append(symLinkObj)

    def createSymLinks(self):
        for symLink in self.symLinks:
            symLink.addSymlink()