from Scripts.Git import Git
from Scripts.DriveMounting import DriveCollection
from Scripts.Packages import Packages
from Scripts.ServerConfig import ServerConfig
from Scripts.FolderSyncing import FolderSyncing
from Scripts.SystemLinks import SymLinks
from Scripts.ConfigWriter import ConfigOptions
from Scripts import Themes
from Configuration import Configuration

class main:
    def main(self):
        config = Configuration()

        git = Git(config.gitConfig)
        git.install()
        git.configure()
        git.authorise(config.gitToken)

        serverConfig = ServerConfig(config.serverConfig)
        serverConfig.setupSmbConfig(config.smbConfig)

        drives = DriveCollection(config.drives)
        drives.addFstabEntries(serverConfig)

        packages = Packages(config.packages)
        packages.refreshRepositories()
        packages.installPackages()

        symLinks = SymLinks(config.symLinks)
        symLinks.createSymLinks()

        configOptions = ConfigOptions(config.configOptions)
        configOptions.SetOptions()

        grubTheme = Themes.Grub(config.grubOptions)
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