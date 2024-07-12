import Packages
import FileManaging
import Command

def installAndConfigureGit(gitConfigYaml):
    gitConfig = FileManaging.importYaml(gitConfigYaml)
    Packages.installZypperPackage("git-core")
    Packages.installZypperPackage("gh")
    Command.configureGit(gitConfig["email"], gitConfig["name"])

    with open("/home/joep/Linux_Install/manjaro_i3/.env/.gittoken", "r") as token_file:
      Command.authorizeGithub(token_file)