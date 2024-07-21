class SymLinkSet:
    def __init__(self, json_object: dict) -> None:

        self.source = json_object["source"]
        self.destination = json_object["destination"]