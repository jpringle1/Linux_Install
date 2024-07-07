import os

class Prerequisites:
    @staticmethod
    def installAndConfigureGit(gitConfigDirectory, gitConfigYaml, githubTokenFile):
        gitConfig = FileManaging.importYaml(gitConfigDirectory + "/" + gitConfigYaml)
        Packages.installZypperPackage("git-core, gh")
        os.popen(f'git config --global user.email {gitConfig["email"]}')
        os.popen(f'git config --global user.name {gitConfig["name"]}')
        os.popen(f'gh auth login --with-token < {gitConfigDirectory}/{githubTokenFile}')