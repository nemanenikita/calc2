"""Function to read CSV"""
import pandas as pd
# from writecsv import writecsv
from tests.absolutepath import absolutepath

#pylint: disable = too-few-public-methods
#pylint: disable = invalid-name
out_file = "tests/output_csv_files/output2.csv"


class Read:
    """Read csv class"""
    # def readcsv(filepath, operation):
    #     file = pd.read_csv(filepath)
    #     return writecsv(file, operation, filepath)

    @staticmethod
    def csvreader():
        """read csv"""
        file = pd.read_csv(absolutepath(out_file))
        return file
