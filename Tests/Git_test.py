import pytest
from unittest.mock import patch

from Scripts.Git.Git import Subprocesses, Git

# Test Git class
class TestGit:
    @pytest.fixture
    def git_instance(self):
        name = "joe"
        email = "test@email.com"
        credentialsJson = {"name": name, "email": email}
        return Git(credentialsJson)

    def test_init(self, git_instance):
        assert git_instance.email == "test@email.com"
        assert git_instance.name == "joe"

    @patch('Scripts.Packages.Package')
    def test_install(self, mock_installPackage):
        repository = "Zypper"
        packages = ["git-core", "gh"]
        
        Git.install()

        assert mock_installPackage.call_count == 2
        # TODO: assert that functions are called with correct packages
        mock_installPackage.assert_called_with(packages[0])

    @patch.object(Subprocesses, 'configureGitName')
    @patch.object(Subprocesses, 'configureGitEmail')
    def test_configure(self, mock_configureGitEmail, mock_configureGitName, git_instance):
        email = "test@example.com"
        name = "Test User"

        git_instance.configure()

        mock_configureGitEmail.assert_called_once_with(email)
        mock_configureGitName.assert_called_once_with(name)

    def test_authorise(self):
        pytest.fail("Not implemented")


# Test Subprocesses class
class TestSubprocesses:
    @patch('subprocess.run')
    def test_authoriseGit(self, mock_run):
        token = "token"
        subprocess = Subprocesses()

        subprocess.authoriseGit(token)
        
        mock_run.assert_called_once_with(["gh", "auth", "login", "--with-token"], stdin=token, check=True)

    @patch('subprocess.run')
    def test_configureGitEmail(self, mock_run):
        email = "email"
        subprocess = Subprocesses()
        
        subprocess.configureGitEmail(email)
        
        mock_run.assert_called_once_with(["git", "config", "--global", "user.email", email], check=True)

    @patch('subprocess.run')
    def test_configureGitName(self, mock_run):
        name = "name"
        subprocess = Subprocesses()
        
        subprocess.configureGitName(name)
        
        mock_run.assert_called_once_with(["git", "config", "--global", "user.name", name], check=True)
