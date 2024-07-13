import subprocess
from Models.Configs import GitConfig

def configureGit(gitConfig: GitConfig):
    subprocess.run(["git", "config", "--global", "user.email", gitConfig.email], check=True)
    subprocess.run(["git", "config", "--global", "user.name", gitConfig.name], check=True)

def authorizeGithub(token_file):
    subprocess.run(["gh", "auth", "login", "--with-token"], stdin=token_file, check=True)

def IscsiTargetDiscovery(nasIpAddress):
    subprocess.run([
        "sudo", 
        "iscsiadm", 
        "-m", 
        "discovery", 
        "-t", 
        "sendtargets", 
        "-p", 
        nasIpAddress],
        check=True)

def IscsiLogin(targetName, nasIpAddress):
    subprocess.run([
        "sudo", 
        "iscsiadm", 
        "--mode", 
        "node", 
        "--targetname", 
        targetName,
        "--portal",
        nasIpAddress,
        "--login",
        ],
        check=True) 
    
def IscsiFormatDrive(mountPoint):
    subprocess.run(["sudo", "mkfs.ext4", "/dev/" + mountPoint], check=True) #I THINK THIS FORMATS THE DRIVE

def systemCtlReload():
    subprocess.run(["systemctl", "daemon-reload"], check=True)

def fstabMountDrives():
    subprocess.run(["sudo", "mount", "-a"], check=True)

def zypperInstallPackage(package):
    subprocess.run(["sudo", "zypper", "in", "-y", package], check=True)

def flatpakInstallPackage(package):
    subprocess.run(["flatpak", "-y", "install", package], check=True)

def refreshRepositories():
    subprocess.run(["sudo", "zypper", "--gpg-auto-import-keys" ,"ref"], check=True)

def refreshGrub():
    subprocess.run([
        "sudo", 
        "grub-mkconfig", 
        "-o",
        "/boot/grub/grub.cfg"],
        check=True)