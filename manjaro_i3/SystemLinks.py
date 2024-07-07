import os

class SystemLinks:
    @staticmethod
    def deleteSymlink(destinationPath):
        if os.path.isfile(destinationPath):
            os.remove(destinationPath)

    @staticmethod
    def addSymlink(sourcePath, destinationPath):
        commandExecution = os.popen(f'sudo ln -s {destinationPath} {sourcePath}')
        print(commandExecution.read())
        print(commandExecution.close())

    @classmethod
    def addAllSymlinks(cls, symlinksYaml):
        symlinks = FileManaging.importYaml(symlinksYaml)
        for directory in symlinks:
            for symlink in directory["links"]:
                sourcePath = directory["sourceDirectory"] + symlink["sourceName"]
                destinationPath = directory["destinationDirectory"] + symlink["destinationName"]
                cls.deleteSymlink(destinationPath)
                cls.addSymlink(sourcePath, destinationPath)