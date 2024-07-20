from typing import List

from Models.ConfigOption import ConfigOption
from Models.ConfigSectionSet import ConfigSectionSet

class ConfigOptionCollection:
    def __init__(
            self, 
            configSectionSet: ConfigSectionSet) -> None:

        self.options: List[ConfigOption] = []

        for sectionSet in configSectionSet.sections:
            for optionSet in sectionSet.options:
                optionObj = ConfigOption(
                    configSectionSet.filepath,
                    sectionSet.section,
                    optionSet.option,
                    optionSet.value
                )

                self.options.append(optionObj)

    def SetOptions(self):
        for option in self.options:
            option.SetOption()