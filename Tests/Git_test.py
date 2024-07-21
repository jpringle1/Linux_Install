import json
import pytest

from Models import GitCredentials
from Scripts.Git import GitSubprocesses
from Scripts.Git import Git
from Scripts.Packages import Package

@pytest.fixture
def git_credentials():
    data = {
        'name': 'joe',
        'email': 'test@email.com',
        'token': '123456789'
    }
    jsonData = json.dumps(data)
    return GitCredentials(jsonData)

def test_init(git_credentials):
    assert git_credentials.email == "test@email.com"
    assert git_credentials.name == "joe"
    assert git_credentials.token == '123456789'

def test_install_calls_installPackage(mocker):
    packages = ["git-core", "gh"]
    mock_install_package = mocker.patch.object(Package, 'installPackage')
    
    Git.install()
    
    assert mock_install_package.call_count == len(packages)
    mock_install_package.assert_any_call()

def test_configure(mocker, git_credentials):
    mock_configure_git = mocker.patch.object(GitSubprocesses, 'configureGit')
    git = Git(git_credentials)
    
    git.configure()

    mock_configure_git.assert_called_once_with(git_credentials.email, git_credentials.name)

def test_authorise(mocker, git_credentials):
    mock_authorise_git = mocker.patch.object(GitSubprocesses, 'authoriseGit')
    git = Git(git_credentials)

    git.authorise()

    mock_authorise_git.assert_called_once_with(git_credentials.token)
    