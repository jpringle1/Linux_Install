import os
import Packages
import FileManaging

class Prerequisites:
    @staticmethod
    def installAndConfigureGit(gitConfigDirectory, gitConfigYaml):
        gitConfig = FileManaging.importYaml(gitConfigDirectory + "/" + gitConfigYaml)
        Packages.installZypperPackage("git-core, gh")
        os.popen(f'git config --global user.email {gitConfig["email"]}')
        os.popen(f'git config --global user.name {gitConfig["name"]}')
        os.popen(f'gh auth login --with-token {gitConfig["token"]}')