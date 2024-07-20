class FolderSyncSet:
    def __init__(self, json_object: dict) -> None:

        self.program = json_object["program"]
        self.local = json_object["local"]
        self.remote = json_object["remote"]