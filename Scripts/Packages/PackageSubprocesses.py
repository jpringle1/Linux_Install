import subprocess

class PackageSubprocesses:
    def zypperInstallPackage(self, packageName):
        subprocess.run(["sudo", "zypper", "in", "-y", packageName], check=True)

    def flatpakInstallPackage(self, packageName):
        subprocess.run(["flatpak", "-y", "install", packageName], check=True)

    def refreshRepositories(self):
        subprocess.run(["sudo", "zypper", "--gpg-auto-import-keys", "ref"], check=True)