import os
import FileManaging
import subprocess

subprocess.run([""], check=True)

def writeToFstabAndMount(mountString, mountPoint):
    with open("/etc/fstab", "a") as fstab:
        fstab.write(mountString + "\n")
    os.rmdir(f'/mnt/{mountPoint}')
    os.mkdir(f'/mnt/{mountPoint}')

def getExt4MountString(drive, mountPoint):
    return f'UUID={drive}    /mnt/{mountPoint}    ext4    defaults    0    1'

def getCifsMountString(drive, mountPoint, nasIpAddress):
    return f'//{nasIpAddress["serverIp"]}/{drive} /mnt/{mountPoint} cifs credentials={nasIpAddress["credentials"]},uid=1000,gid=1000 0 0'

def getIscsiMountString(drive, mountPoint, nasIpAddress):
    subprocess.run([
        "sudo", 
        "iscsiadm", 
        "--mode", 
        "node", 
        "--targetname", 
        nasIpAddress["targetName"],
        "--portal",
        nasIpAddress["serverIp"],
        "--login",
        ],
        check=True)    
    subprocess.run(["sudo", "mkfs.ext4", "/dev/"+{mountPoint}], check=True)
    return f'/dev/{drive} /mnt/{mountPoint} ext4 _netdev,rw 0 0'

def setupSmbCredentials(smbcredentials):
    f = open(smbcredentials["location"], "w")
    f.write(f"username={smbcredentials['username']}\n")
    f.write(f"password={smbcredentials['password']}\n")
    f.write(f"domain={smbcredentials['domain']}")
    f.close()

def mountDrives(drivesYaml, serverConfig):
    drives = FileManaging.importYaml(drivesYaml)
    serverConfig = FileManaging.importYaml(serverConfig)

    setupSmbCredentials(serverConfig["smbcredentials"])

    for drive in drives["ext4"]:
        mountString = getExt4MountString(drive["drive"], drive["mountpoint"])
        writeToFstabAndMount(mountString, drive["mountpoint"])

    for drive in drives["cifs"]:
        mountString = getCifsMountString(drive["drive"], drive["mountpoint"], serverConfig["nasIpAddress"])
        writeToFstabAndMount(mountString, drive["mountpoint"])

    for drive in drives["iscsi"]:
        mountString = getIscsiMountString(drive["drive"], drive["mountpoint"], serverConfig["nasIpAddress"])
        writeToFstabAndMount(mountString, drive["mountpoint"])
        
        subprocess.run(["systemctl", "daemon-reload"], check=True)
        subprocess.run(["sudo", "mount", "-a"], check=True)
