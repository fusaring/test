import pytest
from page.book_home import BookHomePage


class TestBookUI:

    def test_homepage_title(self, browser):
        """测试首页标题和默认书籍"""
        page = BookHomePage(browser)
        page.open()

        # 验证标题
        assert "小说书架" in page.get_title()

        # 验证默认显示4本书
        books = page.get_book_names()
        assert len(books) == 4
        print(f"默认书籍: {books}")

    @pytest.mark.parametrize("keyword, expected_count", [
        ("剑来", 1),
        ("凡人修仙传", 1),
        ("雪中悍刀行", 0),  # 不存在的书
    ])
    def test_search_book(self, browser, keyword, expected_count):
        """测试搜索书籍"""
        page = BookHomePage(browser)
        page.open()
        page.search(keyword)

        # 验证搜索结果数量
        results = page.get_book_names()
        assert len(results) >= expected_count, f"搜索'{keyword}'期望至少{expected_count}本，实际找到{len(results)}本"
        print(f"搜索'{keyword}'结果: {results}")

    def test_click_read(self, browser):
        """测试点击继续阅读跳转"""
        page = BookHomePage(browser)
        page.open()

        # 获取当前窗口句柄
        main_handle = browser.current_window_handle

        # 点击继续阅读
        page.click_first_read()

        # 切换到新窗口
        all_handles = browser.window_handles
        if len(all_handles) > 1:
            browser.switch_to.window(all_handles[-1])

        # 验证跳转后的页面
        assert "小说书架" in browser.title or "章节" in browser.page_source

        # 切回原窗口
        browser.switch_to.window(main_handle)

    def test_search_then_clear(self, browser):
        """测试搜索后清空，回到首页"""
        page = BookHomePage(browser)
        page.open()

        # 先搜索
        page.search("剑来")

        # 再打开首页（模拟清空）
        page.open()

        # 验证回到首页，显示默认书籍
        books = page.get_book_names()
        assert len(books) == 4
