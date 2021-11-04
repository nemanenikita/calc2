"""Testing the Calculator"""
import pprint

import pytest

from calculator.calculator import Calculator

#this is how you define a function that will run
# each time you pass it to a test, it is called a fixture
@pytest.fixture(name="clear_history")
def clear_history_test():
    """Testing clear history calculator"""
    return Calculator.clear_history()

def test_calculator_add(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)
    assert clear_history

def test_clear_history(clear_history):
    """Testing clear history of the calculator"""
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.clear_history() is True
    assert Calculator.history_count() == 0
    assert clear_history

def test_count_history(clear_history):
    """Testing count history of the calculator"""
    assert Calculator.history_count() == 0
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.history_count() == 2
    assert clear_history

def test_get_last_calculation_result(clear_history):
    """Testing last calculation result the calculator"""
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_last_calculation_added_to_history() == 5
    assert clear_history

def test_get_first_calculation_result(clear_history):
    """Testing first calculation result calculator"""
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_first_calculation_added_to_history() == 4
    assert clear_history

def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(1, 2) == -1
    assert clear_history

def test_calculator_multiply(clear_history):
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1,2) == 2
    assert clear_history

def test_calculator_division(clear_history):
    """test division of 2 numbers"""
    assert Calculator.divide_numbers(4,2) == 2
    assert clear_history

def test_calculator_division_exception():
    """ Testing division exception for division by zero"""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide_numbers(1,0)
