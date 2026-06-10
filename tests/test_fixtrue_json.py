import pytest
import json
from pathlib import Path
json_path = Path(__file__).parent.parent/ "utilities" / "test_data.json"
with open(json_path, encoding="utf-8") as f:
    test_data = json.load(f)

@pytest.fixture(params=test_data)
def book_data(request):
    res= request.param
    yield res
    print(f"  已清理测试数据: {res}")
    res.clear()  # 测试结束后清空数据，模拟资源释放的过程
    


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
    def search(self, keyword):
        # 等待搜索框可输入
        search_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "q"))
        )
        # 输入关键词
        search_box.clear()
        search_box.send_keys(keyword)
        
        # 点击搜索按钮
        search_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        search_button.click()
        
        # 等待搜索结果加载（关键词至少前2个字出现在页面中）
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), keyword[:2])
        )



import pytest
import requests

@pytest.mark.api
@pytest.mark.parametrize('username, password, expected_code, expected_msg', [
    ("admin", "123456", 200, "success"),
    ("user", "wrongpassword", 401, "fail"),
    ("nonexistent", "password", 401, "fail")
])
def test_login(username, password, expected_code,expected_msg):
    response = requests.post("https://example.com/api/login", json={"username": username, "password": password})
    assert response.status_code == expected_code, f"预期HTTP状态码{expected_code}，实际得到: {response.status_code}"
    assert response.json()["msg"] == expected_msg, f"预期消息{expected_msg}，实际得到: {response.json()['msg']}"



class TestDivide:
    def divide(self, a, b):
        if b == 0:
            raise ValueError("除数不能为0")
        return a / b

    def test_normal_division(self):
        assert self.divide(10, 2) == 5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="除数不能为0"):
            self.divide(10, 0)

    @pytest.mark.parametrize("a, b, expected", [
        (9, 3, 3),
        (7, 2, 3.5)
    ])
    def test_parametrized_division(self, a, b, expected):
        assert self.divide(a, b) == expected 



# from locust import HttpUser, task, between

# class WebsiteUser(HttpUser):
#     wait_time = between(1, 3)
#     host = "https://example.com"
#     @task(1)
#     def visit_homepage(self):
#         res=self.client.get("/", name="访问首页", catch_response=True)
#         if res.status_code == 200:
#             res.success()
#         else:
#             res.failure(f"访问首页失败，状态码: {res.status_code}")
#     @task(3)
#     def search_api(self):   
#         res=self.client.get("/search?q=python", name="搜索接口", catch_response=True)
#         if res.status_code == 200:
#             res.success()
#         else:
#             res.failure(f"搜索接口失败，状态码: {res.status_code}")     

# locust --headless -u 10 -r 2 --run-time 10s

@pytest.mark.weather
class TestSearchBaiDu:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options

    def test_search_weather(self):
        options = self.Options()
        options.add_experimental_option('detach', True)  # 运行结束后保持浏览器打开
        service = self.Service(executable_path="chromedriver.exe")
        driver = self.webdriver.Chrome(service=service, options=options)
        driver.get("https://www.baidu.com")
        WebDriverWait(driver, 10).until(
            self.EC.visibility_of_element_located((self.By.ID, "kw"))
        ).send_keys("天气")
        WebDriverWait(driver, 10).until(
            self.EC.element_to_be_clickable((self.By.ID, "su"))
        ).click()
        WebDriverWait(driver, 10).until(
            self.EC.element_to_be_clickable((self.By.PARTIAL_LINK_TEXT, "天气网"))
        ).click()
        import os
        save_dir = os.path.join(os.path.dirname(__file__), "report", "screenshots")
        os.makedirs(save_dir, exist_ok=True)
        driver.save_screenshot(os.path.join(save_dir, "baidu_weather.png"))