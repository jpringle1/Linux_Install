import shutil
import os
import Command
from git import Repo

from Models.Configs import ConfigOptions
from Scripts import ConfigWriter

def applyGrubTheme(configOptions: ConfigOptions):
    themesDirectory = "/usr/share/grub/themes"
    repo_dir = "/home/joep/"
    git_url = "https://github.com/catppuccin/grub.git"

    Repo.clone_from(git_url, repo_dir)

    os.mkdir(themesDirectory)
    shutil.copy(repo_dir + "grub/src/*", themesDirectory)

    ConfigWriter.SetOptions(configOptions)

    Command.refreshGrub()