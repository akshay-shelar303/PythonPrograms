import pytest

##def test_greater():
##   num = 100
##   assert num > 100
##
##def test_greater_equal():
##   num = 100
##   assert num >= 100
##
##def test_less():
##   num = 100
##   assert num < 200


def myfun():
    a = 10
    b = 20
    return a < b


def test_myfun():
    assert myfun()
