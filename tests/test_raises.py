import pytest


def divide(a, b):
    """一个简单的除法函数"""
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b


def login(username, password):
    """模拟登录函数"""
    if not username:
        raise ValueError("用户名不能为空")
    if not password:
        raise ValueError("密码不能为空")
    if username == "admin" and password == "123456":
        return "登录成功"
    raise ValueError("用户名或密码错误")

@pytest.mark.raises
class TestRaises:

    def test_divide_normal(self):
        """正常情况"""
        assert divide(10, 2) == 5

    def test_divide_by_zero(self):
        """断言抛出了ValueError"""
        with pytest.raises(ValueError):
            divide(10, 0)

    def test_divide_error_message(self):
        """断言异常信息包含指定文字"""
        with pytest.raises(ValueError, match="除数不能为0"):
            divide(10, 0)

    def test_login_empty_username(self):
        """断言空用户名"""
        with pytest.raises(ValueError, match="用户名不能为空"):
            login("", "123456")

    def test_login_wrong_password(self):
        """断言密码错误"""
        with pytest.raises(ValueError, match="用户名或密码错误"):
            login("admin", "wrong")

    def test_login_success(self):
        """正常登录"""
        result = login("admin", "123456")
        assert result == "登录成功"
    def test_login_empty_password(self):
        """断言空密码"""
        with pytest.raises(ValueError, match="密码不能为空"):
            login('admin','')