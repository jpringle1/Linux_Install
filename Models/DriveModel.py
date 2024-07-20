class DriveModel:
    def __init__(self, json_data: dict) -> None:

        self.driveName: str = json_data["driveName"]
        self.mountPoint: str = json_data["mountPoint"]