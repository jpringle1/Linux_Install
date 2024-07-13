import os
from Models.SymLinks import SymLinks

def deleteSymlink(destinationPath):
    if os.path.isfile(destinationPath):
        os.remove(destinationPath)

def addSymlink(sourcePath, destinationPath):
    commandExecution = os.popen(f'sudo ln -s {destinationPath} {sourcePath}')
    print(commandExecution.read())
    print(commandExecution.close())

def addAllSymlinks(symLinks: SymLinks):
    for entry in symLinks:
        for symlink in entry.links:
            sourcePath = entry.sourceDirectory + symlink.sourceName
            destinationPath = entry.destinationDirectory + symlink.destinationName
            deleteSymlink(destinationPath)
            addSymlink(sourcePath, destinationPath)