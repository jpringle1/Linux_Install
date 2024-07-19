import json
from Scripts.Git import GitSubprocesses
from Scripts.Packages.Package import Package

class Git:
  def __init__(
        self, 
        json_data: dict) -> None:
      
    self.email = json_data.get("email")
    self.name = json_data.get("name")

  def __repr__(self) -> str:
      return f"Git(email={self.email}, name={self.name})"

  def install():
    Package("git-core", "Zypper").installPackage()
    Package("gh", "Zypper").installPackage()

  def configure(self):
    GitSubprocesses.configureGitEmail(self.email)
    GitSubprocesses.configureGitName(self.name)

  def authorise(self, token_filepath):
    with open(token_filepath, "r") as token_file:
      GitSubprocesses.authoriseGit(token_file)