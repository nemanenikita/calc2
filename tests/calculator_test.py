"""Testing the Calculator"""
import pytest
import pandas as pd
from calc.calculator import Calculator
from calc.history.calculations import Calculations
@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()
#You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple
    value = []
    data = pd.read_csv("addition_15values.csv")
    df = pd.DataFrame(data)
    print("DF--", df)
    for i in df[-1]:
        value.append(i)
    Calculator.add_numbers(value)
    assert Calculator.get_last_result_value() == df[-1]
def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple
    value = []
    data = pd.read_csv("subtraction1.csv")
    df = pd.DataFrame(data)
    print("DF--", df)
    for i in df[-1]:
        value.append(i)
    Calculator.subtract_numbers(value)
    assert Calculator.get_last_result_value() == df[-1]

def test_calculator_multiply_static(clear_history_fixture):
    """Testing the multiply method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple
    value = []
    data = pd.read_csv("multiplication.csv")
    df = pd.DataFrame(data)
    print("DF--", df)
    for i in df[-1]:
        value.append(i)
    Calculator.multiply_numbers(value)
    assert Calculator.get_last_result_value() == df[-1]

def test_calculator_divide_static(clear_history_fixture):
    """Testing the divide method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    # using Tuple instead of args because we can pack as much data as we need into the tuple
    my_tuple=(2.0,1.0)
    Calculator.divide_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 0.5
