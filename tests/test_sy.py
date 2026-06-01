import pytest

@pytest.mark.sy
class TestSy:
    def add(self,a, b):
        return a + b
    def test_add(self):
        assert self.add(1, 1) == 2, "测试失败，1+1不等于2"
    def str_cl(self,str_input):
        strc=int(str_input)
        return strc
    @pytest.mark.xfail(reason="数据中有违规的类型")
    @pytest.mark.parametrize("strs", ["123", "abc", "456",12346])
    def test_str(self,strs):
        assert isinstance(self.str_cl(strs), int), "测试失败，'{}'没有被转换为整数".format(strs)
        assert len(str(strs)) <= 3, "测试失败，'{}'的长度不为3".format(strs)

    @pytest.mark.ccc
    def test_02(self,number_list):
        assert sum(number_list) == 15, "测试失败，数字列表的和不为15"