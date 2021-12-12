"""Calculation history Class"""
import pandas as pd
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from tests.csvwrite import csvwriter

#pylint: disable=invalid-name
class Calculations:
    """Calculation history Class"""
    history = []

    @staticmethod
    def clear_history():
        """ clear the history items"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """ get the length of history items"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation_object():
        """ get the last calculation from history"""
        return Calculations.history[-1]

    @staticmethod
    def get_last_calculation_result():
        """ get the last calculation from history"""
        return Calculations.get_last_calculation_object().get_result()

    @staticmethod
    def get_first_calculation():
        """ get the first calculation from history"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation_from_history(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def create_dataframe_to_write(val1, val2, result, operation):
        """appends values and operation to history"""
        df_to_write = pd.DataFrame(columns=['value_1', 'value_2', 'result', 'operation performed'])
        df_to_write = df_to_write.append({'value_1': val1,
                                          'value_2': val2,
                                          'result': result,
                                          'operation performed': operation},
                                         ignore_index=True)
        return csvwriter(df_to_write)

    @staticmethod
    def add_calculation_to_history(calculation):
        """ get a specific calculation from history"""
        Calculations.history.append(calculation)
        return Calculations.history

    @staticmethod
    def readHistoryFromCSV():
        """Read the history from csv and put it into the history """


    @staticmethod
    def writeHistoryToCSV():
        """Write the history to csv file"""
    # pylint: disable=too-few-public-methods
    @staticmethod
    def add_calculation(calculation):
        """ get a generic calculation from history"""
        Calculations.clear_history()
        return Calculations.history.append(calculation)
    @staticmethod
    def add_addition_calculation_to_history(values):
        """create an addition and add object to history using factory method create"""
        Calculations.add_calculation(Addition.create(values))
        #Get the result of the calculation
        return True
    @staticmethod
    def add_subtraction_calculation_to_history(values):
        """create a subtraction object to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(values))
        return True
    @staticmethod
    def add_multiplication_calculation_to_history(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(values))
        return True
