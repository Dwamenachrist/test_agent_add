import pytest
from add import add_numbers, subtract_numbers

def test_add_numbers():
    # Test with positive integers
    assert add_numbers(5, 3) == 8
    # Test with negative integers
    assert add_numbers(-1, -1) == -2
    # Test with zero
    assert add_numbers(0, 0) == 0
    assert add_numbers(0, 5) == 5
    
def test_subtract_numbers():
    # Test with positive integers
    assert subtract_numbers(10, 4) == 6
    # Test with negative integers
    assert subtract_numbers(-1, -1) == 0
    # Test with zero
    assert subtract_numbers(0, 0) == 0
    assert subtract_numbers(5, 0) == 5

if __name__ == "__main__":
    pytest.main()