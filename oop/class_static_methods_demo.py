class MathTools:
    pi = 3.14159  # Class-level attribute

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    @classmethod
    def get_calculation_type(cls):
        return cls.calculation_type

   
     
