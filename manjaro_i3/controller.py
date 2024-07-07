import yaml, os
from pathlib import Path
from shutil import copyfile

cwd = os.getcwd()

class FileManaging:
    @staticmethod
    def importYaml(fileName):
        with open(cwd + "/resources/" + fileName + ".yaml", 'r') as stream:
            return yaml.safe_load(stream)


class Preqrequisites:
    @staticmethod
    def installAndConfigureGit(gitConfigDirectory, gitConfigYaml, githubTokenFile):
        gitConfig = FileManaging.importYaml(gitConfigDirectory + "/" + gitConfigYaml)
        Packages.installZypperPackage("git-core, gh")
        os.popen(f'git config --global user.email {gitConfig["email"]}')
        os.popen(f'git config --global user.name {gitConfig["name"]}')
        os.popen(f'gh auth login --with-token < {gitConfigDirectory}/{githubTokenFile}')

class DriveMounting:
    @staticmethod
    def writeToFstabAndMount(mountString, mountPoint):
        with open("/etc/fstab", "a") as fstab:
            fstab.write(mountString + "\n")
        os.rmdir(f'/mnt/{mountPoint}')
        os.mkdir(f'/mnt/{mountPoint}')

    @staticmethod
    def getExt4MountString(drive, mountPoint):
        return f'UUID={drive}    /mnt/{mountPoint}    ext4    defaults    0    1'

    @staticmethod
    def getCifsMountString(drive, mountPoint, serverConfig):
        return f'//{serverConfig["serverIp"]}/{drive} /mnt/{mountPoint} cifs credentials={serverConfig["credentials"]},uid=1000,gid=1000 0 0'

    @staticmethod
    def getIscsiMountString(drive, mountPoint, serverConfig):
        os.popen(f'sudo iscsiadm --mode node --targetname {serverConfig["targetName"]} --portal {serverConfig["serverIp"]} --login && sudo mkfs.ext4 /dev/{mountPoint}')
        return f'/dev/{drive} /mnt/{mountPoint} ext4 _netdev,rw 0 0'
    
    @classmethod
    def mountDrives(cls, drivesYaml):
        drives = FileManaging.importYaml(drivesYaml)
        
        copyfile(cwd + "/driveMounting/.smbcredentials", "/home/joep/.smbcredentials")

        for drive in drives["ext4"]:
            mountString = cls.getExt4MountString(drive["drive"], drive["mountpoint"])
            cls.writeToFstabAndMount(mountString, drive["mountpoint"])

        for drive in drives["cifs"]:
            mountString = cls.getCifsMountString(drive["drive"], drive["mountpoint"])
            cls.writeToFstabAndMount(mountString, drive["mountpoint"])

        for drive in drives["iscsi"]:
            mountString = cls.getIscsiMountString(drive["drive"], drive["mountpoint"])
            cls.writeToFstabAndMount(mountString, drive["mountpoint"])
        
        os.popen("systemctl daemon-reload && sudo mount -a")

class Packages:
    @staticmethod
    def addRepository():
        print("")

    @staticmethod
    def refreshRepositories():
        os.popen("sudo zypper -y ref")

    @staticmethod
    def installZypperPackage(package):
        os.popen(f"sudo zypper -y in {package}")

    @staticmethod
    def installFlatpak(package):
        os.popen(f"flatpak -y install {package}")

    @classmethod
    def installPackages(cls, packagesYamlFile):
        packages = FileManaging.importYaml(packagesYamlFile)
        cls.addRepository()
        cls.refreshRepositories()
        for package in packages["zypper"]:
            cls.installZypperPackage(package)
        for package in packages["flatpak"]:
            cls.installFlatpakPackage(package)

class SystemLinks:
    @staticmethod
    def deleteSymlink(destinationPath):
        if os.path.isfile(destinationPath):
            os.remove(destinationPath)

    @staticmethod
    def addSymlink(sourcePath, destinationPath):
        commandExecution = os.popen(f'sudo ln -s {destinationPath} {sourcePath}')
        print(commandExecution.read())
        print(commandExecution.close())

    @classmethod
    def addAllSymlinks(cls, symlinksYaml):
        symlinks = FileManaging.importYaml(symlinksYaml)
        for directory in symlinks:
            for symlink in directory["links"]:
                sourcePath = directory["sourceDirectory"] + symlink["sourceName"]
                destinationPath = directory["destinationDirectory"] + symlink["destinationName"]
                cls.deleteSymlink(destinationPath)
                cls.addSymlink(sourcePath, destinationPath)

class UserInterface:
    print("not impleneted")
    # GRUB
    # Splash Screen
    # Login Screen
    # Konsole

    # @staticmethod
    # def setupKdeTheming(scriptDirectory):

    # def removeShutdownLoginOptions

class Configurations:
    print("not impleneted")
    #key_bindings

class FolderSyncing:
    print("not implemented")
        
os.popen(f'sh {cwd}/resources/userInterface/kde.sh')
os.popen(f'sh {cwd}/resources/userInterface/removeShutdownOptions.sh')
os.popen(f'sh {cwd}/resources/configurations/key_bindings.sh')