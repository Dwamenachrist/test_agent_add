import pytest
from add import add_numbers, subtract_numbers

# Normal Cases

def test_add_positive_numbers():
    assert add_numbers(3, 5) == 8


def test_subtract_positive_numbers():
    assert subtract_numbers(10, 4) == 6

# Edge Cases

def test_add_large_numbers():
    assert add_numbers(10**10, 10**10) == 20000000000


def test_subtract_large_numbers():
    assert subtract_numbers(10**10, 5) == 9999999995


def test_add_zero():
    assert add_numbers(0, 5) == 5


def test_subtract_to_zero():
    assert subtract_numbers(5, 5) == 0

# Error Handling

def test_add_non_integer():
    with pytest.raises(TypeError):
        add_numbers("string", 10)


def test_subtract_non_integer():
    with pytest.raises(TypeError):
        subtract_numbers(None, 5)


def test_add_invalid_input():
    with pytest.raises(TypeError):
        add_numbers([1,2], 5)