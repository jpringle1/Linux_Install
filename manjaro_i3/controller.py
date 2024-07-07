import yaml, os
from pathlib import Path
from shutil import copyfile

cwd = os.getcwd()

# Next to do: refactor all files into OOP, aka turn them into libraries and or classes that the main file can use as methods. Will need to think about how i'm going to handle the config files'

class FileManaging:
    @staticmethod
    def importYaml(yamlFile, directory):
        with open(cwd + directory + yamlFile, 'r') as stream:
            return yaml.safe_load(stream)

class DriveMounting:

class Packages:

class SystemLinks:

class FolderSyncing:

class UserInterface:

class Configurations: