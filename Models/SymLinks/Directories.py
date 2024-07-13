from typing import List
from SymLink import SymLink

class Directories:
    def __init__(self, sourceDirectory: str, destinationDirectory: str, links: List[SymLink]) -> None:
        self.sourceDirectory = sourceDirectory
        self.destinationDirectory = destinationDirectory
        self.links: List[SymLink] = links

    def __repr__(self) -> str:
        return f"Directories(sourceDirectory={self.sourceDirectory}, destinationDirectory={self.destinationDirectory}, links={self.links})"
