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
    def multiply(cls, a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    @classmethod
    def get_calculation_type(cls):
        return cls.calculation_type

    @staticmethod
    def add(a, b):
        """Add two numbers without needing class or instance data."""
        return a + b

    @staticmethod
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b

    @classmethod
    def circle_area(cls, radius):
        """Calculate the area of a circle using class-level pi."""
        return cls.pi * radius * radius

    @classmethod
    def circle_circumference(cls, radius):
        """Calculate circumference using class-level pi."""
        return 2 * cls.pi * radius
