class Sync:
    def __init__(self, program: str, local: str, remote: str) -> None:
        self.program = program
        self.local = local
        self.remote = remote

    def __repr__(self) -> str:
        return f"Sync(program={self.program}, local={self.local}, remote={self.remote})"