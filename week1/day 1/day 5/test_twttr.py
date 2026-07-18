from twttr import shorten


def test_something():
    assert shorten("hello") == "hll"

def test_numbers():
    assert shorten(",123:") == ",123:"

def test_vowels():
    assert shorten("aeiou") == ""

def test_novowels():
    assert shorten("gnhn") == "gnhn"