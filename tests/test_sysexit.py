import pytest

def func():
    raise Exception("哎呀，我报错了")

def test_exception():
    with pytest.raises(SystemExit):
        func()