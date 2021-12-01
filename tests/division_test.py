"""Testing Multiplication"""
import os
import logging
import calc.log as log
import pandas as pd
import pytest

from calc.calculations.division import Division
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s','%Y-%m-%d %H:%M:%S')
fh = logging.FileHandler('exception.log')
fh.setFormatter(f)
logger.addHandler(fh)
BASE_DIR = os.path.dirname(os.path.realpath(__file__)) # Get Current Working Directory


def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    filename = "Input Files/division.csv"
    path = os.path.join(BASE_DIR,filename)
    data_frame = pd.read_csv(path)
    for index, row in data_frame.iterrows():
        values = (row.value1, row.value2)
        division= Division.create(values)

        try:
            # Assert
            division_result = data_frame['result'][index].round(decimals=5)
            log.saveData(filename, row.value1, "/", row.value2, division_result)
            assert division.get_result() == division_result
        except ZeroDivisionError:
            with pytest.raises(ZeroDivisionError):
                logger.error("Zero Division Error occurred")
                    # return appendFile
                assert division.get_result() is True
