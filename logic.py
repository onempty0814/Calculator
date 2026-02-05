# Import math module as tools
import math

"""
A class for encapsulation
"""
class CalculatorLogic:

    """
    Dunder function
    """
    def __init__(self):
        pass

    """
    Addition, subtraction, multiplication and division functions
    """
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
        # Catch division by zero error
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    """
    Trigonometric functions
    """
    # The built-in math functions require radians as input
    @staticmethod
    def sin_deg(angle):
        return math.sin(math.radians(angle))
    @staticmethod
    def cos_deg(angle):
        return math.cos(math.radians(angle))
    @staticmethod
    def tan_deg(angle):
        return math.tan(math.radians(angle))


    """
    Inverse trigonometric functions (returns angles)
    """
    @staticmethod
    def arcsin_deg(value):
        return math.degrees(math.asin(value))
    @staticmethod
    def arccos_deg(value):
        return math.degrees(math.acos(value))
    @staticmethod
    def arctan_deg(value):
        return math.degrees(math.atan(value))

    """
    Exponentiation including the square and the square roots functions
    """
    @staticmethod
    def square(a):
        return a ** 2
    @staticmethod
    def sqrt(a):
        # Negative numbers cannot be square roots
        if a < 0:
            raise ValueError("Invalid Input")
        return math.sqrt(a)

    """
    Factorial function
    """
    @staticmethod
    def factorial(a):
        if a < 0:
            raise ValueError("Invalid Input")
        return math.factorial(int(a))

    """
    Logarithmic functions
    """
    @staticmethod
    def logarithm(a, base):
        if a < 0 or base < 0:
            raise ValueError("Invalid Input")
        return math.log(a, base)

    @staticmethod
    def natural_logarithm(a):
        if a < 0:
            raise ValueError("Invalid Input")
        return math.log(a,math.e)

    """
    Percent function
    """
    @staticmethod
    def percent(a):
        return a / 100
