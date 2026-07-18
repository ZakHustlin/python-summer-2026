from vanity import is_valid

def test_firsttwo():
    assert is_valid("H9OHJ") != True

def test_characternumber():
    assert is_valid("H") == False

def test_punctuation():
    assert is_valid("HJ5,6") == False

def test_numbersafterletters():
    assert is_valid("HJ56K4") == False

def test_numberzero():
    assert is_valid("HJ098") == False