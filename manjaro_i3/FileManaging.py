import yaml

def importYaml(fileName):
    with open(fileName + ".yaml", 'r') as stream:
        return yaml.safe_load(stream)
