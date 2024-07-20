import subprocess

class DriveSubprocesses:
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

    def mount():
        subprocess.run(["sudo", "mount", "-a"], check=True)