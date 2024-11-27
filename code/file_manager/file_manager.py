from os import mkdir
from pathlib import Path

class FileManager:
    def __init__(
            self
    ) -> None:
        self.cwd = Path.cwd()
        self.base_path = self.get_base_path()
        self.data_folder = self.base_path / "data"

    def get_base_path(
            self
    ) -> Path:
        cwd = Path.cwd()
        while cwd.stem != 'hickathon5':
            cwd = cwd.parent
        return cwd

    def create_folder(
            self,
            folder_path: Path | str
    ) -> None:
        try:
            mkdir(folder_path)
        except FileExistsError:
            pass
        except OSError as error:
            print(error)