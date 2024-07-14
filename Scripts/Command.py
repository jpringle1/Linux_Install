import subprocess
from Models.Configs import GitConfig

def configureGit(gitConfig: GitConfig):
    subprocess.run(["git", "config", "--global", "user.email", gitConfig.email], check=True)
    subprocess.run(["git", "config", "--global", "user.name", gitConfig.name], check=True)

def authorizeGithub(token_file):
    subprocess.run(["gh", "auth", "login", "--with-token"], stdin=token_file, check=True)

def refreshGrub():
    subprocess.run([
        "sudo", 
        "grub2-mkconfig", 
        "-o",
        "/boot/grub2/grub.cfg"],
        check=True)