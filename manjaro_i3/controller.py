import yaml, os
from pathlib import Path

cwd = os.getcwd()

with open("scriptOrder.yaml", 'r') as stream:
    scriptOrder = yaml.safe_load(stream)

for directory in scriptOrder:
    print("in directory:", directory["directory"])
    for script in directory["scripts"]:
        print("running script:", script )
        if script[-2:] == "sh":
            os.popen(f'.{cwd}/{directory}/{script}')
        elif script[-2:] == "py":
            path = cwd + "/" + directory["directory"] + "/" + script
            print(path)
            exec(open(path).read())

# Next to do: refactor all files into OOP, aka turn them into libraries and or classes that the main file can use as methods. Will need to think about how i'm going to handle the config files'


class DriveMounting:

class Packages:

class SystemLinks:

class FolderSyncing:

class UserInterface:

class Configurations: