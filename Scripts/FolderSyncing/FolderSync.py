class FolderSync:
    def __init__(self,
                 local: str, 
                 remote: str) -> None:
        self.local: str = local
        self.remote: str = remote