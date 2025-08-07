import pytest
from add import add_numbers, subtract_numbers

def test_add_numbers():
    # Normal cases
    assert add_numbers(3, 2) == 5
    assert add_numbers(0, 5) == 5
    assert add_numbers(-3, -2) == -5
    
    # Edge cases
    assert add_numbers(-3, 5) == 2
    assert add_numbers(0, -5) == -5
    assert add_numbers(0.1, 0.2) == 0.3
    
    # Type error cases
    with pytest.raises(TypeError):
        add_numbers("3", 2)
    with pytest.raises(TypeError):
        add_numbers([1], 2)
    with pytest.raises(TypeError):
        add_numbers(None, 2)


def test_subtract_numbers():
    # Normal cases
    assert subtract_numbers(5, 2) == 3
    assert subtract_numbers(5, 0) == 5
    assert subtract_numbers(5, -2) == 7
    
    # Edge cases
    assert subtract_numbers(-3, 2) == -5
    assert subtract_numbers(-5, 0) == -5
    assert subtract_numbers(0.5, 0.2) == 0.3
    
    # Type error cases
    with pytest.raises(TypeError):
        subtract_numbers("5", 2)
    with pytest.raises(TypeError):
        subtract_numbers([1], 2)
    with pytest.raises(TypeError):
        subtract_numbers(2, None)