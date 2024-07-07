import os
import FileManaging

def deleteSymlink(destinationPath):
    if os.path.isfile(destinationPath):
        os.remove(destinationPath)

def addSymlink(sourcePath, destinationPath):
    commandExecution = os.popen(f'sudo ln -s {destinationPath} {sourcePath}')
    print(commandExecution.read())
    print(commandExecution.close())

def addAllSymlinks(symlinksYaml):
    symlinks = FileManaging.importYaml(symlinksYaml)
    for directory in symlinks:
        for symlink in directory["links"]:
            sourcePath = directory["sourceDirectory"] + symlink["sourceName"]
            destinationPath = directory["destinationDirectory"] + symlink["destinationName"]
            deleteSymlink(destinationPath)
            addSymlink(sourcePath, destinationPath)