import pytest
from add import add_numbers, subtract_numbers


# Test cases for add_numbers

def test_add_two_positive_integers():
    assert add_numbers(5, 3) == 8


def test_add_two_negative_integers():
    assert add_numbers(-5, -3) == -8


def test_add_positive_and_negative_integer():
    assert add_numbers(5, -3) == 2


def test_add_zero_to_number():
    assert add_numbers(0, 5) == 5


def test_add_two_zeros():
    assert add_numbers(0, 0) == 0


def test_add_integer_and_float():
    assert add_numbers(5, 2.5) == 7.5


def test_add_large_integers():
    assert add_numbers(10**18, 10**18) == 2000000000000000000


# Test cases for subtract_numbers

def test_subtract_two_positive_integers():
    assert subtract_numbers(5, 3) == 2


def test_subtract_negative_integer_from_positive():
    assert subtract_numbers(5, -3) == 8


def test_subtract_two_negative_integers():
    assert subtract_numbers(-5, -3) == -2


def test_subtract_zero_from_number():
    assert subtract_numbers(5, 0) == 5


def test_subtract_number_from_itself():
    assert subtract_numbers(5, 5) == 0


def test_subtract_float_from_integer():
    assert subtract_numbers(5, 2.5) == 2.5


def test_subtract_large_integers():
    assert subtract_numbers(10**18, 10**17) == 900000000000000000