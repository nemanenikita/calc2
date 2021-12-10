"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController,Page4Controller, Page5Controller
from app.controllers.index_controller import Page1Controller, Page2Controller,Page3Controller
from app.controllers.calculator_controller import CalculatorController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/page1", methods=["GET"])
def page1_get():
    return Page1Controller.get()

@app.route("/page2", methods=["GET"])
def page2_get():
    return Page2Controller.get()

@app.route("/page3", methods=["GET"])
def page3_get():
    return Page3Controller.get()

@app.route("/page4", methods=["GET"])
def page4_get():
    return Page4Controller.get()

@app.route("/page5", methods=["GET"])
def page5_get():
    return Page5Controller.get()
