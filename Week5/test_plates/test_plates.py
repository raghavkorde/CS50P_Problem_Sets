from plates import is_valid

def test_length():
    assert is_valid("CS500993") == False
    assert is_valid(" ") == False
    assert is_valid("A") == False

def test_character():
    assert is_valid("CS5@") == False
    assert is_valid("CS5%") == False

def test_placement():
    assert is_valid("CS50S") == False
    assert is_valid("50CS") == False
    assert is_valid("CS05") == False

def test_startWithTwoCahr():
    assert is_valid("A503") == False
