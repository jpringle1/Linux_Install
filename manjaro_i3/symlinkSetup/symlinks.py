import yaml, os
from pathlib import Path

namespace = "/mnt/LinuxSetup/Linux_Install/manjaro_i3/system_prep/symlinkSetup/"

with open(namespace + "symlinks.yaml", 'r') as stream:
    symlinks = yaml.safe_load(stream)

for group in symlinks:
    for symlink in group["links"]:
        try:
            os.remove(f'~/{symlink["source"]}')
        except:
            Path(f'~/{symlink["source"]}').mkdir(parents=True, exist_ok=True)
            os.remove(f'~/{symlink["source"]}')

        commandExecution = os.popen(f'sudo ln -s {group["directory"]}{symlink["destination"]} ~/{symlink["source"]}')
        print(commandExecution.read())
        print(commandExecution.close())