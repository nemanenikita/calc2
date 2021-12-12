"""Testing Multiplication"""
import os

import pandas as pd
from calc import log
from calc.calculations.multiplication import Multiplication
from tests.absolutepath import absolutepath
# pylint: disable=unused-variable

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) # Get Current Working Directory

#pylint: disable=unsubscriptable-object
def test_calculation_multiplication():
    """testing that our calculator has a static method for addition"""
    #Arrange
    file = pd.read_csv(absolutepath('Input Files/multiplication.csv'))
    filename = "Input Files/multiplication.csv"
    # path = os.path.join(BASE_DIR,filename)
    # data_frame = pd.read_csv(path)
    for index, row in file.iterrows():
        values = (row.value1, row.value2)
        record_num = index
        multiplication= Multiplication.create(values)
        multiplication_result = file["result"][index]
        log.save_data(filename, row.value1, "*", row.value2, multiplication_result,record_num)
        assert multiplication.get_result() == multiplication_result
