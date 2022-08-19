"""
Calculator module with sum, substract, multiply and divide functions
"""


def sum_numbers(num_a, num_b):
    """
    Sum of two numbers
    """
    return num_a + num_b


def subtract(munuend, subtrahend):
    """
    Substraction of two numbers
    """
    return munuend - subtrahend


def multiply(multiplicand, multiplier):
    """
    Multiplication of two numbers
    """
    return multiplicand * multiplier


def divide(dividend, divisor):
    """
    Division operation

    Raise: ValueError when the divisor is zero
    """
    if divisor == 0:
        raise ValueError('Can not divide by zero!')

    return dividend / divisor
