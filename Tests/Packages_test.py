import unittest
from unittest.mock import Mock, mock_open
from Scripts.Packages import Package, Repository, Packages, Subprocesses

import unittest
from unittest.mock import patch

class TestPackage(unittest.TestCase):
     
    @patch.object(Subprocesses, 'zypperInstallPackage')
    def test_installPackage_whenGivenZypperPackage_callsZypperInstallPackage(self, mock_zypperInstallPackage):
        packageName = "package-name"
        repository = "Zypper"
        package = Package(packageName, repository)

        package.installPackage()

        mock_zypperInstallPackage.assert_called_once_with(packageName)

    @patch.object(Subprocesses, 'flatpakInstallPackage')
    def test_installPackage_whenGivenFlatpakPackage_callsFlatpakInstallPackage(self, mock_flatpakInstallPackage):
        packageName = "package-name"
        repository = "Flatpak"
        package = Package(packageName, repository)

        package.installPackage()

        mock_flatpakInstallPackage.assert_called_once_with(packageName)

class TestPackages(unittest.TestCase):
    def create_package_json(self):
        return [
            {"repository": "Zypper", "packages": ["pkg1", "pkg2"]},
            {"repository": "Flatpak", "packages": ["pkg3"]}
        ]

    def test_init_importsJson(self):
        package_data = self.create_package_json()

        packages = Packages(package_data)

        self.assertEqual(len(packages), 3)
        self.assertEqual(packages[0].packageName, "pkg1")
        self.assertEqual(packages[0].repository, Repository.Zypper)
        self.assertEqual(packages[2].packageName, "pkg3")
        self.assertEqual(packages[2].repository, Repository.Flatpak)
    
    @patch('Scripts.Packages.Package.installPackage')
    def test_installPackages_callsInstallPackagesForEveryPackage(self, mock_installPackage):
        package_data = self.create_package_json()
        packages = Packages(package_data)

        packages.installPackages()
        
        self.assertEqual(mock_installPackage.call_count, 3)

class TestSubprocesses(unittest.TestCase):
    @patch('subprocess.run')
    def test_refreshRepositories_refreshesRepositories(self, mock_run):
        Subprocesses.refreshRepositories(self)
        
        mock_run.assert_called_once_with(["sudo", "zypper", "--gpg-auto-import-keys", "ref"], check=True)

    @patch('subprocess.run')
    def test_zypperInstallPackage_installsPackage(self, mock_run):
        packageName = "test-package"

        Subprocesses.zypperInstallPackage(self, packageName)
        
        mock_run.assert_called_once_with(["sudo", "zypper", "in", "-y", packageName], check=True)
    
    @patch('subprocess.run')
    def test_flatpakInstallPackage_installsPackage(self, mock_run):
        packageName = "test-package"
        
        Subprocesses.flatpakInstallPackage(self, packageName)
        
        mock_run.assert_called_once_with(["flatpak", "-y", "install", packageName], check=True)

if __name__ == '__main__':
    unittest.main()