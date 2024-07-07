import os
import Packages
import FileManaging
import subprocess


def installAndConfigureGit(gitConfigYaml):
    gitConfig = FileManaging.importYaml(gitConfigYaml)
    Packages.installZypperPackage("git-core")
    Packages.installZypperPackage("gh")
    subprocess.run(["git", "config", "--global", "user.email", gitConfig["email"]], check=True)
    subprocess.run(["git", "config", "--global", "user.name", gitConfig["name"]], check=True)
    subprocess.run(["gh", "auth", "login", "--with-token", gitConfig["token"]], check=True)