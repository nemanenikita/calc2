"""Testing Multiplication"""
import os
import logging
import pandas as pd
import pytest
from calc import log
from tests.absolutepath import absolutepath
# pylint: disable=unused-variable

#pylint: disable=unsubscriptable-object
from calc.calculations.division import Division
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s','%Y-%m-%d %H:%M:%S')
fh = logging.FileHandler('exception.log')
fh.setFormatter(f)
logger.addHandler(fh)
# BASE_DIR = os.path.dirname(os.path.realpath(__file__)) # Get Current Working Directory

def test_calculation_division():
    """testing that our calculator has a static method for addition"""
    #Arrange
    file = pd.read_csv(absolutepath('Input Files/division.csv'))
    filename = "Input Files/division.csv"
    # path = os.path.join(BASE_DIR,filename)
    # data_frame = pd.read_csv(path)
    for index, row in file.iterrows():
        values = (row.value1, row.value2)
        record_num=index
        division= Division.create(values)

        try:
            # Assert
            division_result = file['result'][index].round(decimals=5)
            log.save_data(filename, row.value1, "/", row.value2, division_result,record_num)
            assert division.get_result() == division_result

        except ZeroDivisionError:
            with pytest.raises(ZeroDivisionError):
                # logger.info(f'Filename:{filename} - Record Number:{record_num}')
                logger.error(f'Filename:{filename} - Record Number:{record_num}' "  Zero Division Error occurred")
                    # return appendFile
                assert division.get_result() is True
