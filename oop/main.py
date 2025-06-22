# main.py

from class_static_methods_demo import Calculator

def main():
    print("Calculation Type:", Calculator.get_calculation_type())
    print("Add:", Calculator.add(5, 3))
    print("Subtract:", Calculator.subtract(5, 3))
    print("Multiply:", Calculator.multiply(5, 3))
    print("Divide:", Calculator.divide(5, 0))
