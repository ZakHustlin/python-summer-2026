from NUMB3RS import validate

def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    
def test_invalid():   
    assert validate("257.3.5.6") == False
    assert validate("hello.hello.5.6") == False