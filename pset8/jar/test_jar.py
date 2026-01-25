from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"


def test_deposit_overflow():
    jar = Jar(capacity=5)
    with pytest.raises(ValueError):
        jar.deposit(6)


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5


def excess_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2