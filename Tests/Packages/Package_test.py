import pytest
from pytest_mock import mocker
from Scripts.Enums.Repository import Repository
from Scripts.Packages.Package import Package
from Scripts.Packages.PackageSubprocesses import PackageSubprocesses

def test_installPackage_whenGivenZypperPackage_callsZypperInstallPackage(mocker):
    packageName = "package-name"
    repository = Repository.Zypper
    package = Package(packageName, repository)
    
    mock_zypperInstallPackage = mocker.patch.object(PackageSubprocesses, 'zypperInstallPackage')
    
    package.installPackage()
    
    mock_zypperInstallPackage.assert_called_once_with(packageName)

def test_installPackage_whenGivenFlatpakPackage_callsFlatpakInstallPackage(mocker):
    packageName = "package-name"
    repository = Repository.Flatpak
    package = Package(packageName, repository)
    
    mock_flatpakInstallPackage = mocker.patch.object(PackageSubprocesses, 'flatpakInstallPackage')

    package.installPackage()
    
    mock_flatpakInstallPackage.assert_called_once_with(packageName)
