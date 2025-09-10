"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

import pytest

from calculator import Calculator


@pytest.fixture(name="calculator")
def fixture_calculator():
    return Calculator()


def test_app(calculator: Calculator):

    EXPECTED_HELLO_MSG = "== Calculatrice v1.0 =="

    assert EXPECTED_HELLO_MSG == calculator.get_hello_message()


def test_addition(calculator: Calculator):
    assert calculator.addition(2, 3) == 5
    assert calculator.last_result == 5


def test_subtraction(calculator: Calculator):
    assert calculator.subtraction(10, 3) == 7
    assert calculator.last_result == 7


def test_multiplication(calculator: Calculator):
    assert calculator.multiplication(4, 3) == 12
    assert calculator.last_result == 12


def test_division_normal(calculator: Calculator):
    assert calculator.division(10, 2) == 5
    assert calculator.last_result == 5


def test_division_by_zero(calculator: Calculator):
    result = calculator.division(10, 0)
    assert result == "Erreur : division par zéro"
    assert calculator.last_result == "Error"
