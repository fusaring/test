import pytest


def test_sample_data(sample_data):
    assert sample_data["name"] == "辉夜"
    assert sample_data["level"] == 99
    print(f"  测试通过: {sample_data['name']} 果然是完美的!")


def test_number_list(number_list):
    assert sum(number_list) == 15
    assert len(number_list) == 5
    print(f"  测试通过: 列表和为{sum(number_list)}")
