import pytest


class Person:

    def __init__(self, name):
        self.name = name

    #  重写之后的 __eq__ 方法要有返回值
    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture(autouse=True)
def call_person():
    pp = Person("玭玭")
    print("\n有人来了，是：" + pp.name)
    return pp


def test_person():
    # assert 是根据返回值来判断是否成功，返回 true 则成功，false 则失败
    assert Person("玭玭") == 1
