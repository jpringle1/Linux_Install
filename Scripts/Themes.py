import json
import shutil
import os
import subprocess
from git import Repo

from Models import ConfigOptions
from Scripts import ConfigWriter

class Grub:
    def __init__(
            self, 
            filepath: str) -> None:
    
        jsonString = open(filepath)
        configOptions = json.loads(jsonString)
        jsonString.close()

        self.configOptions: ConfigOptions = configOptions
        self.themesDirectory = "/usr/share/grub/themes"
        self.repo_dir = "/home/joep/"
        self.git_url = "https://github.com/catppuccin/grub.git"

    def apply(self):
        Repo.clone_from(self.git_url, self.repo_dir)
        os.mkdir(self.themesDirectory)
        shutil.copy(self.repo_dir + "grub/src/*", self.themesDirectory)
        ConfigWriter.SetOptions(self.configOptions)

    def refreshGrub():
        subprocess.run([
            "sudo", 
            "grub2-mkconfig", 
            "-o",
            "/boot/grub2/grub.cfg"],
            check=True)