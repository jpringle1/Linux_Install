import Packages
import Command
from Models.Configs import GitConfig

def installAndConfigureGit(gitConfig: GitConfig):
  Packages.installZypperPackage("git-core")
  Packages.installZypperPackage("gh")
  Command.configureGit(gitConfig)

  with open("/home/joep/Linux_Install/manjaro_i3/.env/.gittoken", "r") as token_file:
    Command.authorizeGithub(token_file)