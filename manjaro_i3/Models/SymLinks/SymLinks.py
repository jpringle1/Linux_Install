import json
from typing import List
from SymLink import SymLink
from Directories import Directories

class SymLinks:
    def __init__(self, filepath: str) -> None:
        with open(filepath, 'r') as file:
            symLinks = json.load(file)
        
        self.directories: List[Directories] = []
        
        for directory in symLinks:
            links = [SymLink(link["sourceName"], link["destinationName"]) for link in directory["links"]]
            directoryObj = Directories(
                directory["sourceDirectory"], 
                directory["destinationDirectory"], 
                links
            )
            self.directories.append(directoryObj)