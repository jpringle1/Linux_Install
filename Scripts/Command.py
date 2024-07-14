import subprocess

def refreshGrub():
    subprocess.run([
        "sudo", 
        "grub2-mkconfig", 
        "-o",
        "/boot/grub2/grub.cfg"],
        check=True)