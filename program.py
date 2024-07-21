from Scripts.Git import Git
from Scripts.Packages import PackageCollection
from Scripts.DriveMounting import DriveCollection
from Scripts.ServerConfig import ServerConfig
from Scripts.FolderSyncing.FolderSyncs import FolderSyncs
from Scripts.SystemLinkSetup.SymLinks import SymLinks
from Scripts.ConfigEditing.ConfigOptionCollection import ConfigOptionCollection
from Scripts.UserInterface.Grub import Grub
from Scripts.UserInterface.Misc import Misc
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

        userInterface = Misc(_config("userInterfaceOptions"))
        userInterface.SetOptions()

        grubTheme = Grub.Grub(_config("grubOptions"))
        grubTheme.apply()
        grubTheme.refreshGrub()

        folderSyncing = FolderSyncs()
        folderSyncing.syncKeyboardShortcuts()

        # TODO:
        # - Test everything.
        #   - unit tests
        #   - integration tests (docker and filepaths)

        # - setup symlinks
        # - setup folder syncs
        # - add "add repositories" function

        # - remove secrets and pycache from github

        # - install iscsitools before mountDrives
        # - setup iscsi drive on boot (currently fstab entry bricks system)