import yaml, os

resources = os.getcwd() + "/resources"

class FileManaging:
    @staticmethod
    def importYaml(fileName):
        with open(resources + "/" + fileName + ".yaml", 'r') as stream:
            return yaml.safe_load(stream)

class Prerequisites:
    @staticmethod
    def installAndConfigureGit(gitConfigDirectory, gitConfigYaml, githubTokenFile):
        gitConfig = FileManaging.importYaml(gitConfigDirectory + "/" + gitConfigYaml)
        Packages.installZypperPackage("git-core, gh")
        os.popen(f'git config --global user.email {gitConfig["email"]}')
        os.popen(f'git config --global user.name {gitConfig["name"]}')
        os.popen(f'gh auth login --with-token < {gitConfigDirectory}/{githubTokenFile}')

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