import yaml, os
from pathlib import Path

namespace = "/mnt/LinuxSetup/Linux_Install/manjaro_i3/packages/"

with open(namespace + "programs.yaml", 'r') as stream:
    packages = yaml.safe_load(stream)

for manager in packages:
    for package in manager["apt"]:
        os.popen(f"sudo apt -y install {package}")
    for package in manager["deb"]:
        os.popen(f'gh release download --pattern "*.deb" --repo https://github.com/{package}')
        os.popen("mv *.deb temp.deb && sudo dpkg -i temp.deb && rm temp.deb")
    for package in manager["flatpak"]:
        os.popen(f"flatpak -y install {package}")