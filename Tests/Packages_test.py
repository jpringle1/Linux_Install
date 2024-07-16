import unittest
from unittest.mock import Mock, mock_open
from Scripts.Packages import Package, Repository, Packages

import unittest
from unittest.mock import patch, call

class TestPackage(unittest.TestCase):
    @patch('subprocess.run')
    def test_zypper_install_package(self, mock_run):
        # Arrange
        packageName = "test-package"
        package = Package(packageName, "Zypper")
        
        # Act
        package.installPackage()
        
        # Assert
        mock_run.assert_called_once_with(["sudo", "zypper", "in", "-y", packageName], check=True)
    
    @patch('subprocess.run')
    def test_flatpak_install_package(self, mock_run):
        # Arrange
        packageName = "test-package"
        package = Package(packageName, "Flatpak")
        
        # Act
        package.installPackage()
        
        # Assert
        mock_run.assert_called_once_with(["flatpak", "-y", "install", packageName], check=True)

class TestPackages(unittest.TestCase):
    def test_init(self):
        # Arrange
        package_data = [
            {"repository": "Zypper", "packages": ["pkg1", "pkg2"]},
            {"repository": "Flatpak", "packages": ["pkg3"]}
        ]

        # Act
        packages = Packages(package_data)
        
        # Assert
        self.assertEqual(len(packages.packages), 3)
        self.assertEqual(packages.packages[0].packageName, "pkg1")
        self.assertEqual(packages.packages[0].repository, Repository.Zypper)
        self.assertEqual(packages.packages[2].packageName, "pkg3")
        self.assertEqual(packages.packages[2].repository, Repository.Flatpak)
    
    @patch('Scripts.Packages.Package.installPackage')
    def test_installPackages(self, mock_installPackage):
        # Arrange
        packages = Packages.__new__(Packages)
        packages.packages = [
            Package("pkg1", "Zypper"),
            Package("pkg2", "Flatpak")
        ]
        
        # Act
        packages.installPackages()
        
        # Assert
        self.assertEqual(mock_installPackage.call_count, 2)
        calls = [unittest.mock.call(), unittest.mock.call()]
        mock_installPackage.assert_has_calls(calls, any_order=True)
    
    @patch('subprocess.run')
    def test_refreshRepositories(self, mock_run):
        # Arrange
        packages = Packages.__new__(Packages)
        
        # Act
        packages.refreshRepositories()
        
        # Assert
        mock_run.assert_called_once_with(["sudo", "zypper", "--gpg-auto-import-keys", "ref"], check=True)