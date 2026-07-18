from bank import value

def test_hello():
    assert value("hello") == "$0"

def test_h():
    assert value("hey") == "$20"

def test_none():
    assert value("") == "$100"

def test_number():
    assert value("45") == "$100"