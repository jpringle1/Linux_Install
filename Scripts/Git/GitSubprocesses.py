import subprocess

class GitSubprocesses:
  def configureGit(self, email: str, name: str):
    subprocess.run(["git", "config", "--global", "user.email", email], check=True)
    subprocess.run(["git", "config", "--global", "user.name", name], check=True)

  def authoriseGit(self, token):
      subprocess.run(["gh", "auth", "login", "--with-token"], stdin=token, check=True)