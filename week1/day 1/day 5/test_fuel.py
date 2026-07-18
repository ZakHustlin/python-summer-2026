from fuel_charge import gauge
from fuel_charge import convert

def test_F():
    assert gauge(100) == "F"