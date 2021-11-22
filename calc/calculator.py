""" This is the increment function"""
from calc.calculations.addition import Addition
from calc.calculations.division import Division
from calc.calculations.multiplication import Multiplication
from calc.calculations.subtraction import Subtraction

from calc.history.calculations import Calculations


class Calculator:
    """ This is the Calculator class"""
    @staticmethod
    def get_last_calculation_from_result():
        """ Last value from calculation"""
        return Calculations.get_last_calculation_result()

    @staticmethod
    def add_numbers(values: tuple):
        """ adds list of numbers"""
        Calculations.add_calculation_to_history(Addition.create(values))
        return True

    @staticmethod
    def subtract_numbers(values: tuple):
        """ adds list of numbers"""
        Calculations.add_calculation_to_history(Subtraction.create(values))
        return True

    @staticmethod
    def multiply_numbers(values: tuple):
        """ adds list of numbers"""
        Calculations.add_calculation_to_history(Multiplication.create(values))
        return True

    @staticmethod
    def divide_numbers(values: tuple):
        """ adds list of numbers"""
        Calculations.add_calculation_to_history(Division.create(values))
        return True
