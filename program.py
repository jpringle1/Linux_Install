from Scripts.Git import Git
from Scripts.Packages import PackageCollection
from Scripts.DriveMounting import DriveCollection
from Scripts.ServerConfig import ServerConfig
from Scripts.FolderSyncing import FolderSyncing
from Scripts.SystemLinks import SymLinks
from Scripts.ConfigWriter import ConfigOptions
from Scripts import Themes
from Configuration import Configuration

class main:
    def main(self):
        _config = Configuration()

        git = Git(_config("gitConfig", ".env"))
        git.install()
        git.configure()
        git.authorise()

        serverConfig = ServerConfig(_config("serverConfig"))
        serverConfig.setupSmbConfig(_config("smbConfig"))

        drives = DriveCollection(_config("drives"))
        drives.addFstabEntries(serverConfig)

        packages = PackageCollection(_config("packages"))
        packages.refreshRepositories()
        packages.installPackages()

        symLinks = SymLinks(_config("symLinks"))
        symLinks.createSymLinks()

        configOptions = ConfigOptions(_config("configOptions"))
        configOptions.SetOptions()

        grubTheme = Themes.Grub(_config("grubOptions"))
        grubTheme.apply()
        grubTheme.refreshGrub()

        folderSyncing = FolderSyncing()
        folderSyncing.syncKeyboardShortcuts()

        # TODO:
        # - Test everything. Shit seems broken since i moved everything into models

        # - setup symlinks
        # - setup folder syncs
        # - add "add repositories" function

        # - setup gitignore
        # - remove secrets and pycache from github

        # - install iscsitools before mountDrives
        # - setup iscsi drive on boot (currently fstab entry bricks system)
        # - setup integration tests maybe?