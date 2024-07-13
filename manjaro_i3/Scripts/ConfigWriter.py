import configparser
from Models.Configs import ConfigOptions
    
def SetOption(filepath, section, option, value):
    config = configparser.ConfigParser()
    config.read(filepath)

    if not config.has_section(section):
        config.add_section(section)

    config.set(section, option, value)
    with open(filepath, "w") as configFile:
        config.write(configFile)

def SetOptions(configOptions: ConfigOptions):
    for option in configOptions:
        SetOption(
            option.filepath, 
            option.section, 
            option.option, 
            option.value)

