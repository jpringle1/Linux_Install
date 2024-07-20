from Scripts.Enums.Repository import Repository
from Scripts.Git.GitSubprocesses import GitSubprocesses
from Scripts.Models.GitCredentials import GitCredentials
from Scripts.Packages.Package import Package

class Git:
  def __init__(
        self, 
        credentials: GitCredentials) -> None:
      
    self.email = credentials.email
    self.name = credentials.name
    self.token = credentials.token

  def __repr__(self) -> str:
      return f"Git(email={self.email}, name={self.name}, token={self.token})"

  def install():
    Package("git-core", Repository.Zypper).installPackage()
    Package("gh", Repository.Zypper).installPackage()

  def configure(self):
    GitSubprocesses.configureGit(self.email, self.name)

  def authorise(self):
    GitSubprocesses.authoriseGit(self.token)