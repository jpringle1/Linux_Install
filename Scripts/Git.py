import json
import subprocess
from Scripts.Packages import Package

class Git:
  def __init__(
        self, 
        filepath: str) -> None:
      
    jsonString = open(filepath + ".json")
    credentials = json.loads(jsonString)
    jsonString.close()
    
    self.email: str = credentials["email"]
    self.name: str = credentials["name"]

    def __repr__(self) -> str:
        return f"Git(email={self.email}, name={self.name})"

  def install():
    Package("git-core", "Zypper").installPackage()
    Package("gh", "Zypper").installPackage()

  def configure(self):
    Subprocesses.confgureGitEmail(self.email)
    Subprocesses.confgureGitName(self.name)

  def authorise(self, token_filepath):
    with open(token_filepath, "r") as token_file:
      Subprocesses.authoriseGit(token_file)

class Subprocesses:
  def confgureGitEmail(self, email: str):
    subprocess.run(["git", "config", "--global", "user.email", email], check=True)

  def configureGitName(self, name: str):
    subprocess.run(["git", "config", "--global", "user.name", name], check=True)

  def authoriseGit(self, token):
      subprocess.run(["gh", "auth", "login", "--with-token"], stdin=token, check=True)
