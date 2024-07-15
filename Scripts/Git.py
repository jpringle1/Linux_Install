import json
import subprocess
from Packages import Package

class Git:
  def __init__(
        self, 
        filepath: str) -> None:
      
    jsonString = open(filepath)
    credentials = json.loads(jsonString)
    jsonString.close()
    
    self.email: str = credentials["email"]
    self.name: str = credentials["name"]

    def __repr__(self) -> str:
        return f"Git(email={self.email}, name={self.name})"

  def install():
    Package("git-core", "zypper").installPackage()
    Package("gh", "zypper").installPackage()

  def configure(self):
    subprocess.run(["git", "config", "--global", "user.email", self.email], check=True)
    subprocess.run(["git", "config", "--global", "user.name", self.name], check=True)

  def authorise(self, token_filepath):
    with open(token_filepath, "r") as token_file:
      subprocess.run(["gh", "auth", "login", "--with-token"], stdin=token_file, check=True)
