"""Testing Addition"""
import os

import pandas as pd

from calc.calculations.addition import Addition

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) # Get Current Working Directory


def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    path = os.path.join(BASE_DIR,"addition1.xlsx")
    df = pd.read_excel(path, names=["value1", "value2", "result"])
    for index, row in df.iterrows():
        values = (row.value1, row.value2)
        addition= Addition.create(values)
        assert addition.get_result() == df["result"][index]

