import yaml

def importYaml(resourcesDir, fileName):
    with open(resourcesDir + "/" + fileName + ".yaml", 'r') as stream:
        return yaml.safe_load(stream)