import json
from typing import List    
from SymLinks import Directories
from Sync import Sync

class Syncs:
    def __init__(self, filepath: str) -> None:
        with open(filepath, 'r') as file:
            syncs = json.load(file)
        self.syncs: List[Sync] = []
        
        for sync in syncs:
            syncObj = Directories(
                sync["program"], 
                sync["local"], 
                sync["remote"]
            )
            self.syncs.append(syncObj)

    def __repr__(self) -> str:
        return f"Syncs(syncs={self.syncs})"
    
    def __getitem__(self, index) -> Sync:
        return self.syncs[index]    
