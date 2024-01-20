import yaml, os
from pathlib import Path

with open("scriptOrder.yaml", 'r') as stream:
    scriptOrder = yaml.safe_load(stream)

for directory in scriptOrder:
    for script in directory:
        if script[-2:] == "sh":
            os.popen(f'./{script}')
        elif script[-2:] == "py":
            exec(open(script).read())

