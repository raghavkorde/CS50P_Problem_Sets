import pytest
from numb3rs import validate

def test_valid_ipv4_addresses():
    assert validate('192.168.0.1')
    assert validate('10.0.0.255')
    assert validate('172.16.31.255')

def test_invalid_ipv4_addresses():
    assert not validate('256.0.0.0')
    assert not validate('0.0.0.0.0')
    assert not validate('192.168.0')
    assert not validate('192.168.0.256')
    assert not validate('192.168.0.-1')
    assert not validate('192.168.0.1.2')