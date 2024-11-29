from os import mkdir
from pathlib import Path
from pandas import read_csv, DataFrame

TRAINING_DATA = 'X_train_Hi5.csv'
TEST_DATA = 'X_test_Hi5.csv'

class FileManager:
    def __init__(
            self
    ) -> None:
        self.cwd = Path.cwd()
        self.base_path = self.get_base_path()
        self.data_folder = self.base_path / "data"
        self.training_data_file = self.data_folder / TRAINING_DATA
        self.test_data_file = self.data_folder / TEST_DATA

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

    def load_training_data(
            self
    ) -> DataFrame:
        return read_csv(self.training_data_file, index_col='row_index')
    
    def load_test_data(
            self
    ) -> DataFrame:
        return read_csv(self.test_data_file, index_col='row_index')

    def load_tiny_training_data(
            self,
            n_rows: int = 100_000
    ) -> DataFrame:
        return read_csv(self.training_data_file, index_col='row_index', nrows=n_rows)
