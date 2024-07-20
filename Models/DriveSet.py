import json
from typing import List

from Enums import DriveType
from Models.DriveModel import DriveModel

class DriveSet:
    def __init__(self, json_data: dict) -> None:
        json_object = json.loads(json_data)

        self.driveType = DriveType(json_object["driveType"])
        self.drives: List[DriveModel] = json_object["drives"]