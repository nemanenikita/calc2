from app.controllers.controller import ControllerBase
from flask import render_template

class IndexController(ControllerBase):
    @staticmethod
    def get():
        return render_template('index.html')

class Page1Controller(ControllerBase):
    @staticmethod
    def get():
        return render_template('page1.html')

class Page2Controller(ControllerBase):
    @staticmethod
    def get():
        return render_template('page2.html')

class Page3Controller(ControllerBase):
    @staticmethod
    def get():
        return render_template('page3.html')

class Page4Controller(ControllerBase):
    @staticmethod
    def get():
        return render_template('page4.html')

class Page5Controller(ControllerBase):
    @staticmethod
    def get():
        return render_template('page5.html')