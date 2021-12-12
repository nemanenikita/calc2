"""Calculator controller"""
#pylint: disable=import-error
#pylint: disable=invalid-name
#pylint: disable=no-name-in-module
#pylint: disable=no-member
#pylint: disable=unused-import
#pylint: disable=wrong-import-order

from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from calc.history.calculations import Calculations
from flask import render_template, request, flash, redirect, url_for
from tests.readcsv import Read

class CalculatorController(ControllerBase):
    """Calculator controller"""
    @staticmethod
    def post():
        """post method"""
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'Please enter value 1 and value 2'

        else:
            flash('You successfully calculated')


            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_calculation_from_result())
            Calculations.create_dataframe_to_write(value1, value2, result, operation)
            df = Read.csvreader()
            return render_template('Results Table.html', value1=value1, value2=value2,
                                   operation=operation,
                                   result=result,tables=[df.to_html(classes='data')],
                                   titles=df.columns.values,
                                   row_data=list(df.values.tolist()), zip=zip)
        return render_template('calculator.html', error=error)
    @staticmethod
    def get():
        """get method"""
        return render_template('calculator.html')
