import unittest
from unittest.mock import patch
from Scripts.Enums.Repository import Repository
from Scripts.Packages.Package import Package
from Scripts.Packages.PackageSubprocesses import PackageSubprocesses

class TestPackage(unittest.TestCase):
      
    @patch.object(PackageSubprocesses, 'zypperInstallPackage')
    def test_installPackage_whenGivenZypperPackage_callsZypperInstallPackage(self, mock_zypperInstallPackage):
        packageName = "package-name"
        repository = Repository.Zypper
        package = Package(packageName, repository)

        package.installPackage()

        mock_zypperInstallPackage.assert_called_once_with(packageName)

    @patch.object(PackageSubprocesses, 'flatpakInstallPackage')
    def test_installPackage_whenGivenFlatpakPackage_callsFlatpakInstallPackage(self, mock_flatpakInstallPackage):
        packageName = "package-name"
        repository = Repository.Flatpak
        package = Package(packageName, repository)

        package.installPackage()

        mock_flatpakInstallPackage.assert_called_once_with(packageName)

if __name__ == '__main__':
    unittest.main()