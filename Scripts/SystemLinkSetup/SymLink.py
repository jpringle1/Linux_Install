import os

class SymLink:
    def __init__(
            self, 
            source: str, 
            destination: str) -> None:
        
        self.source: str = source
        self.destination:str = destination

    def addSymlink(self):
        if os.path.isfile(self.destination):
            os.remove(self.destination)
        
        self._addSymlinkCommand()

    def _addSymlinkCommand(self):
        commandExecution = os.popen(f'sudo ln -s {self.destination} {self.source}')
        print(commandExecution.read())
        print(commandExecution.close())