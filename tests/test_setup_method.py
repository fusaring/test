import pytest


class TestSetupDemo:

    def setup_method(self):
        """每个测试方法执行前都会跑"""
        print("\n[setup_method] 准备工作：打开浏览器 / 连接数据库 / 准备测试环境")
        self.driver = "Chrome 浏览器实例"  # 模拟

    def teardown_method(self):
        """每个测试方法执行后都会跑"""
        print("[teardown_method] 清理工作：关闭浏览器 / 断开连接 / 清理数据")
        self.driver = None

    def test_one(self):
        print(f"  [test_one] 正在使用 {self.driver} 测试登录功能")
        assert self.driver is not None

    def test_two(self):
        print(f"  [test_two] 正在使用 {self.driver} 测试注册功能")
        assert self.driver is not None


class TestSetupClassDemo:

    @classmethod
    def setup_class(cls):
        """整个类只执行一次，在所有测试之前"""
        print("\n[setup_class] 整个类只执行一次：启动浏览器")
        cls.driver = "Chrome 浏览器实例"

    @classmethod
    def teardown_class(cls):
        """整个类只执行一次，在所有测试之后"""
        print("[teardown_class] 整个类只执行一次：关闭浏览器")
        cls.driver = None

    def test_three(self):
        print(f"  [test_three] 测试搜索功能，使用 {self.driver}")
        assert self.driver is not None

    def test_four(self):
        print(f"  [test_four] 测试下单功能，使用 {self.driver}")
        assert self.driver is not None
