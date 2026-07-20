import pytest
from cookies import Jar


def test_normaldeposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3


def test_wrongdeposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(100)

def test_normalwithdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7


def test_wrongwithdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(100)

