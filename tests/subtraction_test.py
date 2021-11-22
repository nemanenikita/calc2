"""Testing Addition"""
import os

import pandas as pd

from calc.calculations.subtraction import Subtraction

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) # Get Current Working Directory


def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    path = os.path.join(BASE_DIR,"subtraction2.xlsx")
    data_frame = pd.read_excel(path, names=["value1", "value2", "result"])
    for index, row in data_frame.iterrows():
        values = (row.value1, row.value2)
        subtraction= Subtraction.create(values)
        assert subtraction.get_result() == data_frame["result"][index]
