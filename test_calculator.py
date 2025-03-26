import pytest
from calculator import add, subtract, multiply, divide, square, power

@pytest.fixture
def calculator_values():
    return {
        "a": 10,
        "b": 5,
        "zero": 0,
        "negative": -3
    }

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(-6, -3) == 2
    
    with pytest.raises(ValueError):
        divide(5, 0)

def test_square():
    assert square(2) == 4
    assert square(-2) == 4
    assert square(0) == 0

def test_power():
    assert power(2, 3) == 8
    assert power(2, 0) == 1
    assert power(2, -1) == 0.5

def test_with_fixture(calculator_values):
    a = calculator_values["a"]
    b = calculator_values["b"]
    
    assert add(a, b) == 15
    assert subtract(a, b) == 5
    assert multiply(a, b) == 50
    assert divide(a, b) == 2

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (8, 4, 2),
    (7, 0, None),  # This should raise an error
])
def test_divide_parametrized(a, b, expected):
    if b == 0:
        with pytest.raises(ValueError):
            divide(a, b)
    else:
        assert divide(a, b) == expected