from typing import List

from Models.FolderSyncSet import FolderSyncSet
from Scripts.FolderSyncing.FolderSync import FolderSync

class FolderSyncs:
    def __init__(self, json_object: List[FolderSyncSet]) -> None:

        self.syncs: List[FolderSync] = []
        
        for sync in json_object:
            syncObj = FolderSync(
                sync.local, 
                sync.remote
            )
            self.syncs.append(syncObj)

    def __getitem__(self, index) -> FolderSync:
        return self.syncs[index]    
    
    # ctrl+alt+arrow = move to beginning/end of line (Home/End)
    # ctrl+shift+alt+arrow =select from cursor to beginning/end of line (Shift+Home/End)
    # meta+space = krunner
    # klipper - bind to mod+v