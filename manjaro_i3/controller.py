import os

resources = os.getcwd() + "/resources"

class UserInterface:
    print("not impleneted")
    # GRUB
    # Splash Screen
    # Login Screen
    # Konsole

    # @staticmethod
    # def setupKdeTheming(scriptDirectory):

    # def removeShutdownLoginOptions

class Configurations:
    print("not impleneted")
    #key_bindings

class FolderSyncing:
    print("not implemented")

Prerequisites.installAndConfigureGit("git", "gitConfig", "myGithubToken.txt")
DriveMounting.mountDrives("drives", "drives")
Packages.installPackages("packages")
SystemLinks.addAllSymlinks("symlinks")

os.popen(f'sh {resources}/userInterface/kde.sh')
os.popen(f'sh {resources}/userInterface/removeShutdownOptions.sh')
os.popen(f'sh {resources}/configurations/key_bindings.sh')