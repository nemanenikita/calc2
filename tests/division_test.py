"""Testing Multiplication"""
import os

import pandas as pd
import pytest

from calc.calculations.division import Division

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) # Get Current Working Directory


def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    path = os.path.join(BASE_DIR,"division1.xlsx")
    data_frame = pd.read_excel(path, names=["value1", "value2", "result"])
    for index, row in data_frame.iterrows():
        values = (row.value1, row.value2)
        division= Division.create(values)

        try:
            # Assert
            assert division.get_result() == data_frame['result'][index].round(decimals=5)
        except ZeroDivisionError:
            with pytest.raises(ZeroDivisionError):
                assert division.get_result() is True
