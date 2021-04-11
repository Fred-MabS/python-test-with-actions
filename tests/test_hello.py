import src.hello as CUT
import pytest


def test_name():
    assert CUT.hello('name') == 'Hello name'

def test_hello():
    assert CUT.hello('Celine') == 'Hello Celine'
