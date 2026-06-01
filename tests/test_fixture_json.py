import pytest
import json
from pathlib import Path


# 1. 先读取 JSON 数据
DATA_PATH = Path(__file__).parent.parent / "utilities" / "test_book.json"
BOOK_CASES = json.load(open(DATA_PATH, encoding="utf-8"))

print(f"从JSON读取到 {len(BOOK_CASES)} 条数据:")
for c in BOOK_CASES:
    print(f"  - {c['keyword']}")


# 2. fixture params 接收 JSON 数据，自动生成多条用例
@pytest.fixture(params=BOOK_CASES)
def book_case(request):
    """每条 JSON 数据生成一条测试用例，带 yield 清理"""
    print(f"\n准备测试: {request.param['keyword']}")
    yield request.param
    print(f"清理完成: {request.param['keyword']}")


# 3. 测试函数直接引用 fixture，不用写 parametrize
class TestBookSearch:

    def test_search(self, browser, book_case):
        """测试搜索书籍"""
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        browser.get("https://yileila.top/flask/book/")
        search_input = browser.find_element(By.NAME, "q")
        search_input.send_keys(book_case["keyword"])
        browser.find_element(By.XPATH, "//button[@type='submit']").click()

        # 验证搜索结果包含关键词
        WebDriverWait(browser, 5).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), book_case["keyword"][:2])
        )
        assert book_case["keyword"][:2] in browser.page_source
