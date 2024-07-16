import unittest
from unittest.mock import Mock, mock_open
from Scripts.Git import Subprocesses

import unittest
from unittest.mock import patch, call

class TestSubprocesses(unittest.TestCase): 
    @patch('subprocess.run')
    def test_authoriseGit(self, mock_run):
        # Arrange
        token = "token"
        subprocess = Subprocesses()

        # Act
        subprocess.authoriseGit(token)
        
        # Assert
        mock_run.assert_called_once_with(["gh", "auth", "login", "--with-token"], stdin=token, check=True)

    @patch('subprocess.run')
    def test_configureGitEmail(self, mock_run):
        # Arrange
        email = "email"
        subprocess = Subprocesses()
        
        # Act
        subprocess.confgureGitEmail(email)
        
        # Assert
        mock_run.assert_called_once_with(["git", "config", "--global", "user.email", email], check=True)

    @patch('subprocess.run')
    def test_configureGitName(self, mock_run):
        # Arrange
        name = "name"
        subprocess = Subprocesses()
        
        # Act
        subprocess.configureGitName(name)
        
        # Assert
        mock_run.assert_called_once_with(["git", "config", "--global", "user.name", name], check=True)        