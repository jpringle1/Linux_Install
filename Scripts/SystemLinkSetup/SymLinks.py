from typing import List

from Models.SymLinkSet import SymLinkSet
from Scripts.SystemLinkSetup.SymLink import SymLink

class SymLinks:
    def __init__(
            self, 
            json_object: List[SymLinkSet]) -> None:
        
        self.symLinks: List[SymLink] = []
        
        for link in json_object:
            symLinkObj = SymLink(
                link.source,
                link.destination
            )

            self.symLinks.append(symLinkObj)

    def createSymLinks(self):
        for symLink in self.symLinks:
            symLink.addSymlink()