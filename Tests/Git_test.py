import unittest
from unittest.mock import Mock, mock_open
from Scripts.Git import Subprocesses, Git

import unittest
from unittest.mock import patch, call
#look into magicMock

class TestGit(unittest.TestCase):
    def test_init(self):
        name = "joe"
        email = "test@email.com"
        credentialsJson = {"name": name, "email": email}

        git = Git(credentialsJson)

        self.assertEqual(git.email, email)
        self.assertEqual(git.name, name)

    @patch('Scripts.Packages.Package')
    def test_install(self, mock_installPackage):
        repository = "Zypper"
        packages = ["git-core", "gh"]
        
        Git.install()

        self.assertEqual(mock_installPackage.call_count, 2)
        # TODO: assert that functions are called with correct packages
        mock_installPackage.assert_called_with(packages[0])

    @patch.object(Subprocesses, 'configureGitName')
    @patch.object(Subprocesses, 'configureGitEmail')
    def test_configure(self, mock_configureGitEmail, mock_configureGitName):
        email = "test@example.com"
        name = "Test User"

        git = Git(json_data)

        git.configure()

        mock_configureGitEmail.assert_called_once_with(email)
        mock_configureGitName.assert_called_once_with(name)

    def test_authorise(self):
        self.fail("Not implemented")

class TestSubprocesses(unittest.TestCase): 
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