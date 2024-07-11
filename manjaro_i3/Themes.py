import shutil
import os
import subprocess
from git import Repo

def applyGrubTheme():
    themesDirectory = "/usr/share/grub/themes"
    repo_dir = "/home/joep/"
    grubDirectory = "/etc/default/grub"
    git_url = "https://github.com/catppuccin/grub.git"

    newThemeSetting = 'GRUB_THEME="/usr/share/grub/themes/catppuccin-frappe-grub-theme/theme.txt"'
    newResolutionSetting = "GRUB_GFXMODE=5120x1440"

    Repo.clone_from(git_url, repo_dir)

    os.mkdir(themesDirectory)
    shutil.copy(repo_dir + "grub/src/*", themesDirectory)

    with open(grubDirectory, "a") as myfile:
        myfile.write(newThemeSetting)
        myfile.write(newResolutionSetting)

    subprocess.run([
        "sudo", 
        "grub-mkconfig", 
        "-o",
        "/boot/grub/grub.cfg"],
        check=True)
    