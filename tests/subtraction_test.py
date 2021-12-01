"""Testing Addition"""
import os
import logging
import calc.log as log
import pandas as pd

from calc.calculations.subtraction import Subtraction

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) # Get Current Working Directory


def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    filename = "Input Files/subtraction.csv"
    path = os.path.join(BASE_DIR,filename)
    data_frame = pd.read_csv(path)
    for index, row in data_frame.iterrows():
        values = (row.value1, row.value2)
        subtraction= Subtraction.create(values)
        subtraction_result = data_frame["result"][index]
        log.saveData(filename, row.value1, "-", row.value2, subtraction_result)
        assert subtraction.get_result() == subtraction_result
