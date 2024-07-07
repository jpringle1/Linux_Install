import os

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