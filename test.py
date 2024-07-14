import configparser

from Models.Configs import ServerConfig, ConfigOptions
from Scripts import ConfigWriter

def setupSmbCredentials(config: ServerConfig):
    with open(config.credentialsDirectory, "w") as f:
        f.write(f"username={config.smbUsername}\n")
        f.write(f"password={config.smbPassword}\n")
        f.write(f"domain={config.smbDomain}")

ConfigWriter.SetOptions(ConfigOptions.ConfigOptions("Resources/smbConfig"))