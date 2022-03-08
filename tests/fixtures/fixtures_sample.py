import pytest


# 水果类，传入水果的名字，代表不同的水果
class Fruit:
    # python 类中的初始化函数，也叫构造函数：
    #       1. 当你创建一个类的实例的时候，这个函数就会自动被调用，当代码执行了 Fruit() 语句时，就会调用
    #       2. 函数名是固定写法，第一个参数必须写上 self
    #       3. 初始化函数可以传递参数
    def __init__(self, name):
        self.name = name

    # python 类中的比较函数：
    #       1. 两个对象的直接用 == 来判断的话，其结果不一定相等，因为如果是同一个类的两个不同的实例，他们的物理地址是不同的，所以此时需要使用 __eq__ 函数
    #       2. 此函数默认由两个参数，一个是 self 一个是 other，用 self 的属性和 other 的属性的进行对比，成功返回 true，失败返回 false
    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture()
def my_fruit():
    print("\n# 我被执行了......")
    return Fruit("apple")


# 果篮函数，把多种水果放到一个 list 中
@pytest.fixture()
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_basket(fruit_basket):
    assert Fruit("apple") in fruit_basket


def test_my_fruit_in_basket2(fruit_basket):
    assert Fruit("orange") in fruit_basket
