from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from calc.history.calculations import Calculations
from flask import render_template, request, flash, redirect, url_for
from tests.readcsv import Read
import pandas as pd

class CalculatorController(ControllerBase):
    @staticmethod
    def post():
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
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result,tables=[df.to_html(classes='data')], titles=df.columns.values, row_data=list(df.values.tolist()), zip=zip)
        return render_template('calculator.html', error=error)
    @staticmethod
    def get():
        return render_template('calculator.html')





