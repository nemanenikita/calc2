"""index controller"""
# pylint: disable=no-name-in-module
#pylint: disable=import-error
#pylint: disable=too-few-public-methods
from flask import render_template
from app.controllers.controller import ControllerBase


class IndexController(ControllerBase):
    """index class"""
    @staticmethod
    def get():
        """getter method"""
        return render_template('index.html')

class Page1Controller(ControllerBase):
    """page class"""
    @staticmethod
    def get():
        """getter method"""
        return render_template('page1.html')

class Page2Controller(ControllerBase):
    """page class"""
    @staticmethod
    def get():
        """getter method"""
        return render_template('page2.html')

class Page3Controller(ControllerBase):
    """page class"""
    @staticmethod
    def get():
        """getter method"""
        return render_template('page3.html')

class Page4Controller(ControllerBase):
    """page class"""
    @staticmethod
    def get():
        """getter method"""
        return render_template('page4.html')

class Page5Controller(ControllerBase):
    """page class"""
    @staticmethod
    def get():
        """getter method"""
        return render_template('page5.html')
