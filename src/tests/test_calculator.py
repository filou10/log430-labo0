"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from src.calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "Calculatrice"

def test_addition_success():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 5

def test_addition_fail():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 3

def test_addition_fail_2():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 4