""" This is the increment function"""
from calc.calculations.addition import Addition

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
