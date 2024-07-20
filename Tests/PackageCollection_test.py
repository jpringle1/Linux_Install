import json
import pytest
from pytest_mock import mocker
from typing import List

from Enums import Repository
from Models import RepositorySet
from Scripts.Packages import PackageCollection

@pytest.fixture
def create_repo_set():
    def _create_repo_set(repository: Repository, packages: List[str]) -> RepositorySet:
        data = {
            'repository': repository.name,
            'packages': packages
        }
        jsonData = json.dumps(data)
        return RepositorySet(jsonData)
    return _create_repo_set

@pytest.mark.parametrize("repository, expected_repo", [
    (Repository.Zypper, Repository.Zypper),
    (Repository.Flatpak, Repository.Flatpak)
])
def test_package_collection_initialization(create_repo_set, repository, expected_repo):
    package_name = "pkg1"
    repo_set = create_repo_set(repository, [package_name])
    package_collection = PackageCollection([repo_set])

    assert len(package_collection) == 1
    package = package_collection[0]
    assert package.packageName == package_name
    assert package.repository == expected_repo

def test_install_packages_calls_install_package_for_every_package(mocker, create_repo_set):
    mock_install_package = mocker.patch('Scripts.Packages.Package.Package.installPackage')
    packages = ["pkg1", "pkg2", "pkg3"]
    repo_set = create_repo_set(Repository.Zypper, packages)
    package_data = [repo_set]
    package_collection = PackageCollection(package_data)

    package_collection.installPackages()
    
    assert mock_install_package.call_count == 3
