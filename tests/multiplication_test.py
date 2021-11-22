"""Testing Multiplication"""
import os

import pandas as pd

from calc.calculations.multiplication import Multiplication

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) # Get Current Working Directory


def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    path = os.path.join(BASE_DIR,"multiplication1.xlsx")
    df = pd.read_excel(path, names=["value1", "value2", "result"])
    for index, row in df.iterrows():
        values = (row.value1, row.value2)
        multiplication= Multiplication.create(values)
        assert multiplication.get_result() == df["result"][index]

