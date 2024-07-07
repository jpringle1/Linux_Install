import Packages
import FileManaging
import subprocess

def installAndConfigureGit(gitConfigYaml):
    gitConfig = FileManaging.importYaml(gitConfigYaml)
    Packages.installZypperPackage("git-core")
    Packages.installZypperPackage("gh")
    subprocess.run(["git", "config", "--global", "user.email", gitConfig["email"]], check=True)
    subprocess.run(["git", "config", "--global", "user.name", gitConfig["name"]], check=True)
    with open("/home/joep/Linux_Install/manjaro_i3/.env/.gittoken", "r") as token_file:
      subprocess.run(["gh", "auth", "login", "--with-token"], stdin=token_file, check=True)
