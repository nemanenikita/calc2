"""This is result controller"""
#pylint: disable=invalid-name
#pylint: disable=no-name-in-module
#pylint: disable=no-member
#pylint: disable=too-few-public-methods
#pylint: disable=wrong-import-order
#pylint: disable=import-error

from app.controllers.controller import ControllerBase
from tests.readcsv import Read
from flask import render_template

class ResultController(ControllerBase):
    """Result controller"""
    @staticmethod
    def get():
        """get method"""
        df = Read.csvreader()
        return render_template('Results Table.html', titles=df.columns.values,
                               row_data=list(df.values.tolist()), zip=zip)
