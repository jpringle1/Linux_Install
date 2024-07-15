import json
from typing import List

class Sync:
    def __init__(self, program: str, local: str, remote: str) -> None:
        self.program = program
        self.local = local
        self.remote = remote

    def __repr__(self) -> str:
        return f"Sync(program={self.program}, local={self.local}, remote={self.remote})"

class Syncs:
    def __init__(self, filepath: str) -> None:
        with open(filepath, 'r') as file:
            syncs = json.load(file)
        self.syncs: List[Sync] = []
        
        for sync in syncs:
            syncObj = List(
                sync["program"], 
                sync["local"], 
                sync["remote"]
            )
            self.syncs.append(syncObj)

    def __repr__(self) -> str:
        return f"Syncs(syncs={self.syncs})"
    
    def __getitem__(self, index) -> Sync:
        return self.syncs[index]    

class FolderSyncing:
    def __init__(self) -> None:
        self.placeholder = ""

    def syncKeyboardShortcuts():
        sync_target = "/home/joep/.config/kglobalshortcutsrc"
        # ctrl+alt+arrow = move to beginning/end of line (Home/End)
        # ctrl+shift+alt+arrow =select from cursor to beginning/end of line (Shift+Home/End)
        # meta+space = krunner
        # klipper - bind to mod+v