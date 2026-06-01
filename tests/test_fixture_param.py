import pytest


# 用 fixture params 做数据驱动
@pytest.fixture(params=[
    (10, 2, 5),
    (10, 0, None),     # 除零，后面断言异常
    (9, 3, 3),
    (7, 2, 3.5),
])
def divide_data(request):
    """返回 (a, b, expected) 三组数据"""
    return request.param


def test_divide(divide_data):
    a, b, expected = divide_data
    if b == 0:
        with pytest.raises(ZeroDivisionError):
            a / b
    else:
        assert a / b == expected
