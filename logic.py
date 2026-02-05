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
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        # Catch division by zero error
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    """
    Trigonometric functions
    """
    # The built-in math functions require radians as input
    def sin_deg(self, angle):
        return math.sin(math.radians(angle))
    def cos_deg(self, angle):
        return math.cos(math.radians(angle))
    def tan_deg(self, angle):
        return math.tan(math.radians(angle))


    """
    Inverse trigonometric functions (returns angles)
    """
    def arcsin_deg(self, value):
        return math.degrees(math.asin(value))
    def arccos_deg(self, value):
        return math.degrees(math.acos(value))
    def arctan_deg(self, value):
        return math.degrees(math.atan(value))

    """
    Exponentiation including the square and the square roots functions
    """
    def square(self, a):
        return a ** 2
    def sqrt(self, a):
        # Negative numbers cannot be square roots
        if a < 0:
            raise ValueError("Invalid Input")
        return math.sqrt(a)

    """
    Factorial function
    """
    def factorial(self, a):
        if a < 0:
            raise ValueError("Invalid Input")
        return math.factorial(int(a))

    """
    Logarithmic functions
    """
    def logarithm(self,a,base):
        if a < 0 or base < 0:
            raise ValueError("Invalid Input")
        return math.log(a, base)

    def natural_logarithm(self,a):
        if a < 0:
            raise ValueError("Invalid Input")
        return math.log(a,math.e)

    """
    Percent function
    """
    def percent(self,a):
        return 100 * a / 100
