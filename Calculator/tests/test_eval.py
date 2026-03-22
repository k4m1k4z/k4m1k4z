import pytest
from GUI.Model import CalculatorModel


@pytest.fixture
def model():
    return CalculatorModel()


# ======================
# TESTS BÁSICOS
# ======================

def test_append(model):
    model.append("2")
    model.append("+")
    model.append("3")
    assert model.expression == "2+3"


def test_clear(model):
    model.append("123")
    model.clear()
    assert model.expression == ""


# ======================
# OPERACIONES
# ======================

def test_addition(model):
    model.append("2+3")
    result = model.evaluate()
    assert result == "5"


def test_subtraction(model):
    model.append("10-4")
    result = model.evaluate()
    assert result == "6"


def test_multiplication(model):
    model.append("3*5")
    result = model.evaluate()
    assert result == "15"


def test_division(model):
    model.append("8/2")
    result = model.evaluate()
    assert result == "4.0"


# ======================
# COMPORTAMIENTO
# ======================

def test_chain_operations(model):
    model.append("2+3")
    result = model.evaluate()
    assert result == "5"

    model.append("*2")
    result = model.evaluate()
    assert result == "10"


def test_error_handling(model):
    model.append("2/0")  # división por cero
    result = model.evaluate()
    assert result == "Error"
    assert model.expression == ""


def test_invalid_expression(model):
    model.append("2++")
    result = model.evaluate()
    assert result == "Error"