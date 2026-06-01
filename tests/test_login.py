import pytest
import json
import time
from pathlib import Path

# 读取JSON测试数据
DATA_PATH = Path(__file__).parent.parent / "utilities" / "test_data.json"
LOGIN_CASES = json.load(open(DATA_PATH, encoding="utf-8"))


# ===== 数据驱动的selenium登录测试 =====

@pytest.mark.skip(reason="API接口未打开，暂时跳过")
class TestBlogLogin:

    @pytest.mark.parametrize("case", LOGIN_CASES)
    def test_login(self, browser, case):
        """数据驱动登录测试"""
        from page.login_api import LoginPage
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By

        page = LoginPage(browser)
        page.login(case["username"], case["password"])
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )  # 等待页面加载完成

        if case["expect"] == "success":
            # 等页面跳转到首页
            WebDriverWait(browser, 5).until(
                EC.url_to_be("http://127.0.0.1:5000/")
            )
            assert "欢迎" in browser.page_source, "登录成功后应显示'欢迎'"
        else:
            # 等错误信息出现（JS异步渲染）
            WebDriverWait(browser, 5).until(
                EC.text_to_be_present_in_element((By.ID, "message"), "错误")
            )
            error_text = page.get_error_text()
            assert "用户名或密码错误" in error_text, f"期望错误信息，实际得到: {error_text}"
