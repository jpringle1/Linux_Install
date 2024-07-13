import json
from typing import List

class Packages:
    def __init__(self, filepath: str) -> None:
        jsonString = open(filepath)
        packages = json.loads(jsonString)
        jsonString.close()
        self.zypper: List[str] = packages["zypper"]
        self.flatpak: List[str] = packages["flatpak"]