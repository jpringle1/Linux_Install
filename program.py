import json
import os

from Scripts.Git import Git
from Scripts.DriveMounting import DriveCollection
from Scripts.Packages import Packages
from Scripts.ServerConfig import ServerConfig
from Scripts.FolderSyncing import FolderSyncing
from Scripts.SystemLinks import SymLinks
from Scripts.ConfigWriter import ConfigOptions
from Scripts import Themes

class main:
    def __init__(self) -> None:
        self.Resources = os.getcwd() + "/Resources/"
        self.Env = os.getcwd() + "/.env/"
        self.GitConfig = "gitConfig.json"
        self.GitToken = ".gittoken"
        self.ServerConfig = "serverConfig.json"
        self.SmbConfig = "smbConfig.json"
        self.Drives = "drives.json"
        self.Packages = "packages.json"
        self.SymLinks = "symLinks.json"
        self.ConfigOptions = "configOptions.json"
        self.GrubOptions = "grubOptions.json"

    def read_json(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def main(self):
        gitJson = self.read_json(self.Resources + self.GitConfig)
        git = Git(gitJson)
        git.install()
        git.configure()
        git.authorise(self.Env + self.GitToken)

        serverConfigJson = self.read_json(self.Resources + self.ServerConfig)
        smbConfigJson = self.read_json(self.Resources + self.SmbConfig)
        serverConfig = ServerConfig(serverConfigJson)
        serverConfig.setupSmbConfig(smbConfigJson)

        drivesJson = self.read_json(self.Resources + self.Drives)
        drives = DriveCollection(drivesJson)
        drives.addFstabEntries(serverConfig)

        packagesJson = self.read_json(self.Resources + self.Packages)
        packages = Packages(packagesJson)
        packages.refreshRepositories()
        packages.installPackages()

        symLinksJson = self.read_json(self.Resources + self.SymLinks)
        symLinks = SymLinks(symLinksJson)
        symLinks.createSymLinks()

        configOptionsJson = self.read_json(self.Resources + self.ConfigOptions)
        configOptions = ConfigOptions(configOptionsJson)
        configOptions.SetOptions()

        grubThemeJson = self.read_json(self.Resources + self.GrubOptions)
        grubTheme = Themes.Grub(grubThemeJson)
        grubTheme.apply()
        grubTheme.refreshGrub()

        folderSyncing = FolderSyncing()
        folderSyncing.syncKeyboardShortcuts()

        # TODO:
        # - Test everything. Shit seems broken since i moved everything into models

        # - setup symlinks
        # - setup folder syncs
        # - add "add repositories" function

        # - refactor configuration file (resourcesDir and envDir, as well as config file names (serverConfig, drives, packages etc))
        # - setup gitignore
        # - remove secrets and pycache from github

        # - install iscsitools before mountDrives
        # - setup iscsi drive on boot (currently fstab entry bricks system)
        # - setup integration tests maybe?