import os
import FileManaging
import subprocess

def writeToFstabAndMount(mountString, mountPoint):
    with open("/etc/fstab", "a") as fstab:
        fstab.write(mountString + "\n")

    if os.path.isdir("/mnt/" + mountPoint):  
        os.rmdir(f'/mnt/{mountPoint}')
    
    os.mkdir(f'/mnt/{mountPoint}')

def getExt4MountString(drive, mountPoint):
    remoteDrive = f'UUID={drive}    '
    localMount = f'/mnt/{mountPoint}    '
    filetype = "ext4    "
    idStrings = "defaults    0    1"

    return remoteDrive + localMount + filetype + idStrings

def getCifsMountString(drive, mountPoint, credentials, nasIpAddress):
    remoteDrive = f'//{nasIpAddress}/{drive} '
    localMount = f'/mnt/{mountPoint} '
    filetype = "cifs "
    credentialsStr = f'credentials={credentials}'
    idStrings = ",uid=1000,gid=1000 0 0"

    return remoteDrive + localMount + filetype + credentialsStr + idStrings

def discoverIscsiTargets(nasIpAddress):
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

def getIscsiMountString(drive, mountPoint, nasIpAddress, targetName):
    discoverIscsiTargets(nasIpAddress)
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
    # subprocess.run(["sudo", "mkfs.ext4", "/dev/" + mountPoint], check=True) I THINK THIS FORMATS THE DRIVE
    return f'/dev/{drive} /mnt/{mountPoint} ext4 _netdev,rw 0 0'

def setupSmbCredentials(smbcredentials, credentialLocation):
    f = open(credentialLocation, "w")
    f.write(f"username={smbcredentials['username']}\n")
    f.write(f"password={smbcredentials['password']}\n")
    f.write(f"domain={smbcredentials['domain']}")
    f.close()

def mountDrives(drivesYaml, serverConfigYaml):
    drives = FileManaging.importYaml(drivesYaml)
    serverConfig = FileManaging.importYaml(serverConfigYaml)

    setupSmbCredentials(serverConfig["smbcredentials"], serverConfig["credentialsLocation"])

    for drive in drives["ext4"]:
        mountString = getExt4MountString(drive["drive"], drive["mountPoint"])
        writeToFstabAndMount(mountString, drive["mountPoint"])

    for drive in drives["cifs"]:
        mountString = getCifsMountString(drive["drive"], drive["mountPoint"], serverConfig["credentialsLocation"], serverConfig["nasIpAddress"])
        writeToFstabAndMount(mountString, drive["mountPoint"])

    for drive in drives["iscsi"]:
        mountString = getIscsiMountString(drive["drive"], drive["mountPoint"], serverConfig["nasIpAddress"], drive["targetName"])
        writeToFstabAndMount(mountString, drive["mountPoint"])
        
    subprocess.run(["systemctl", "daemon-reload"], check=True)
    subprocess.run(["sudo", "mount", "-a"], check=True)