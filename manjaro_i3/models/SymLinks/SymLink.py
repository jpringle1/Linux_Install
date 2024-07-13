class SymLink:
    def __init__(self, sourceName: str, destinationName: str) -> None:
        self.sourceName = sourceName
        self.destinationName = destinationName

    def __repr__(self) -> str:
        return f"SymLink(sourceName={self.sourceName}, destinationName={self.destinationName})"