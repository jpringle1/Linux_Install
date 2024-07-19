import json
import subprocess
from typing import List
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
    Subprocesses.configureGitEmail(self.email)
    Subprocesses.configureGitName(self.name)

  def authorise(self, token_filepath):
    with open(token_filepath, "r") as token_file:
      Subprocesses.authoriseGit(token_file)

class Subprocesses:
  def configureGitEmail(self, email: str):
    subprocess.run(["git", "config", "--global", "user.email", email], check=True)

  def configureGitName(self, name: str):
    subprocess.run(["git", "config", "--global", "user.name", name], check=True)

  def authoriseGit(self, token):
      subprocess.run(["gh", "auth", "login", "--with-token"], stdin=token, check=True)