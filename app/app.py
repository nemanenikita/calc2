"""A simple flask web app"""
#pylint : disable=import-error
#pylint : disable=no-name-in-module
#pylint : disable=unused-import

from flask import Flask, request
from app.controllers.index_controller import IndexController,Page4Controller, Page5Controller
from app.controllers.index_controller import Page1Controller, Page2Controller,Page3Controller
from app.controllers.calculator_controller import CalculatorController
from app.controllers.result_controller import ResultController


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    """index page routing controller"""
    return IndexController.get()

@app.route("/Results Table", methods=['GET'])
def result_get():
    """result page routing to controller"""
    return ResultController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    """Calculator page routing controller"""
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    """Calculator post routing controller"""
    return CalculatorController.post()

@app.route("/page1", methods=["GET"])
def page1_get():
    """Page 1 route"""
    return Page1Controller.get()

@app.route("/page2", methods=["GET"])
def page2_get():
    """Page 2 route"""
    return Page2Controller.get()

@app.route("/page3", methods=["GET"])
def page3_get():
    """Page 3 route"""
    return Page3Controller.get()

@app.route("/page4", methods=["GET"])
def page4_get():
    """Page 4 route"""
    return Page4Controller.get()

@app.route("/page5", methods=["GET"])
def page5_get():
    """Page 5 route"""
    return Page5Controller.get()
