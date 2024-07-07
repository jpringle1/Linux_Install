import yaml

class FileManaging:
    @staticmethod
    def importYaml(resourcesDir, fileName):
        with open(resourcesDir + "/" + fileName + ".yaml", 'r') as stream:
            return yaml.safe_load(stream)