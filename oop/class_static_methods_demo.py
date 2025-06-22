class MathTools:
    pi = 3.14159  # Class-level attribute

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