""" This is the increment function"""
class Calculator:
    """ This is the Calculator class"""
    history = []

    result = 0
    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, value_a):
        """ adds number to result"""
        self.result = self.result + value_a
        return self.result
    # def add_number(value_a,value_b):
    #     """ adds number to result"""
    #     return value_a+value_b

    def subtract_number(self, value_a):
        """ subtract number from result"""
        self.result = self.result - value_a
        return self.result
    # def subtract_number(value_a,value_b):
    #     """ subtract number from result"""
    #     return value_a-value_b
    def multiply_numbers(self, value_a, value_b):
        """ multiply two numbers and store the result"""
        self.result = value_a * value_b
        return self.result
    def divide_numbers(self,value_a, value_b):
        """ divide two numbers and store the result"""
        self.result = value_a / value_b
        return self.result
