import pytest
from src.lcm_calculator import gcd, lcm, lcm_multiple

def test_gcd_basic():
    assert gcd(48, 18) == 6
    assert gcd(54, 24) == 6
    assert gcd(17, 23) == 1

def test_gcd_zero():
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0

def test_gcd_negative():
    assert gcd(-48, 18) == 6
    assert gcd(48, -18) == 6
    assert gcd(-48, -18) == 6

def test_gcd_invalid_input():
    with pytest.raises(ValueError):
        gcd(3.5, 4)
    with pytest.raises(ValueError):
        gcd("12", 4)

def test_lcm_basic():
    assert lcm(4, 6) == 12
    assert lcm(21, 6) == 42
    assert lcm(17, 23) == 391

def test_lcm_zero():
    assert lcm(0, 5) == 0
    assert lcm(5, 0) == 0
    assert lcm(0, 0) == 0

def test_lcm_negative():
    assert lcm(-4, 6) == 12
    assert lcm(4, -6) == 12
    assert lcm(-4, -6) == 12

def test_lcm_invalid_input():
    with pytest.raises(ValueError):
        lcm(3.5, 4)
    with pytest.raises(ValueError):
        lcm("12", 4)

def test_lcm_multiple_basic():
    assert lcm_multiple(2, 3, 4) == 12
    assert lcm_multiple(3, 4, 6) == 12
    assert lcm_multiple(2, 3, 4, 5) == 60

def test_lcm_multiple_single_number():
    assert lcm_multiple(5) == 5
    assert lcm_multiple(42) == 42

def test_lcm_multiple_invalid_input():
    with pytest.raises(ValueError):
        lcm_multiple()
    with pytest.raises(ValueError):
        lcm_multiple(2, 3.5, 4)
    with pytest.raises(ValueError):
        lcm_multiple("2", 3, 4)