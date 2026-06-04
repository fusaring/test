from page.book import SearchBook
import pytest
import json
from pathlib import Path
import requests
book_path=Path(__file__).parent.parent / "utilities" / "test_book.json"
BOOK_CASES = json.load(open(book_path,encoding="utf-8"))

@pytest.mark.book
class TestSearchBook:
    # @pytest.mark.skip(reason="搜索功能正在重构，暂时跳过")
    # @pytest.mark.parametrize("case", BOOK_CASES)
    def test_search_book(self, browser, book_data):
        """测试搜索书籍功能"""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        search_page = SearchBook(browser)
        search_page.search(book_data["keyword"])
        # 等搜索结果加载完毕（等关键词的前两个字出现就说明搜到了）
        WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), book_data["keyword"][:2]))
        assert book_data["keyword"] in browser.page_source, f"搜索结果中应包含'{book_data['keyword']}'"

    # def test_index(self, browser):  
    #     """测试首页功能"""
    #     res=requests.get("https://yileila.top/flask/book/")
    #     assert res.status_code == 200, f"预期状态码200，实际得到: {res.status_code}"
    def test_api_search(self, browser):
        """测试API搜索书籍功能"""
        search_page = SearchBook(browser)
        search_page.open()
        search_page.a_link()
        assert "第" in browser.page_source, "搜索结果中应包含'第'"
    def test_api_search_partial(self, browser):
        """测试API搜索书籍功能"""
        search_page = SearchBook(browser)
        search_page.open()
        search_page.a_link_partial()
        assert "第" in browser.page_source, "搜索结果中应包含'第'"    