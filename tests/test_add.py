import pytest
from add import add_numbers, subtract_numbers

def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(1.5, 2.5) == 4.0
    assert add_numbers(10**6, 10**6) == 2000000
    
    with pytest.raises(TypeError):
        add_numbers("a", 1)
    with pytest.raises(TypeError):
        add_numbers(None, 1)

def test_subtract_numbers():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(3, 5) == -2
    assert subtract_numbers(0, 0) == 0
    assert subtract_numbers(1.5, 0.5) == 1.0
    assert subtract_numbers(10**6, 10**6) == 0
    
    with pytest.raises(TypeError):
        subtract_numbers("a", 1)
    with pytest.raises(TypeError):
        subtract_numbers(None, 1)