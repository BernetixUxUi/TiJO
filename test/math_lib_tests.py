from src.math_lib import find_max, is_perfect

def test_max_none():
    # Arrange
    digits = None

    # Act
    result = max(digits)

    # Assert
    assert result is None, "max(None) should return None"

def test_max_empty():
    digits = []
    result = max(digits)
    assert result is None, "max([]) should return None"

def test_max_single_element():
    digits = [42]
    result = max(digits)
    assert result == 42, "max([42]) should return 42"

def test_max_multiple_elements():
    digits = [1, 3, 9, 2, 8]
    result = max(digits)
    assert result == 9, "max([1, 3, 9, 2, 8]) should return 9"

def test_is_perfect_6():
    digit = 6
    result = is_perfect(digit)
    assert result is True, "6 is a perfect number"

def test_is_perfect_28():
    digit = 28
    result = is_perfect(digit)
    assert result is True, "28 is a perfect number"

def test_is_not_perfect():
    digit = 10
    result = is_perfect(digit)
    assert result is False, "10 is not a perfect number"

def test_is_perfect_negative():
    digit = -6
    result = is_perfect(digit)
    assert result is False, "-6 is not a perfect number"