import json
from typing import List
import unittest
from unittest.mock import patch

from Scripts.Enums.Repository import Repository
from Scripts.Models.RepositorySet import RepositorySet
from Scripts.Packages.PackageCollection import PackageCollection

class TestPackageCollection(unittest.TestCase):

    def test_init_importsObject_zypper(self):
        repository = Repository.Zypper
        package = "pkg1"
        repoSet = Helpers.create_repoSet(repository, [package])
        package_data = [repoSet]
        
        package_collection = PackageCollection(package_data)

        self.assertEqual(len(package_collection), 1)
        self.assertEqual(package_collection[0].packageName, package)
        self.assertEqual(package_collection[0].repository, Repository.Zypper)

    def test_init_importsObject_flatpak(self):
        repository = Repository.Flatpak
        package = "pkg1"
        repoSet = Helpers.create_repoSet(repository, [package])
        package_data = [repoSet]
        
        package_collection = PackageCollection(package_data)

        self.assertEqual(len(package_collection), 1)
        self.assertEqual(package_collection[0].packageName, package)
        self.assertEqual(package_collection[0].repository, Repository.Flatpak)
    
    @patch('Scripts.Packages.Package.Package.installPackage')
    def test_installPackages_callsInstallPackagesForEveryPackage(self, mock_installPackage):
        packages = ["pkg1", "pkg2", "pkg3"]
        repoSet = Helpers.create_repoSet(Repository.Zypper, packages)
        package_data = [repoSet]
        package_collection = PackageCollection([package_data])

        package_collection.installPackages()
        
        self.assertEqual(mock_installPackage.call_count, 3)

class Helpers:
    
    @staticmethod
    def create_repoSet(repository: Repository, packages: List[str]) -> RepositorySet:
        data = {
            'repository': repository.name,
            'packages': packages
        }

        jsonData = json.dumps(data)

        return RepositorySet(jsonData)