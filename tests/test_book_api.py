import pytest
import requests

BASE_URL = "https://yileila.top/flask"


class TestBookAPI:

    def test_homepage_api(self):
        """测试首页API响应"""
        resp = requests.get(f"{BASE_URL}/book/", timeout=10)
        assert resp.status_code == 200
        assert "小说书架" in resp.text

    @pytest.mark.parametrize("keyword, expected", [
        ("剑来", True),
        ("凡人修仙传", True),
        ("不存在的书啊啊啊", False),
    ])
    def test_search_api(self, keyword, expected):
        """测试搜索API"""
        resp = requests.get(f"{BASE_URL}/book/", params={"q": keyword}, timeout=10)
        assert resp.status_code == 200
        if expected:
            assert keyword in resp.text
        else:
            assert keyword not in resp.text
    @pytest.mark.resapi
    def test_read_page_api(self):
        """测试阅读页面API"""
        resp = requests.get(f"{BASE_URL}/book/read/4/2", timeout=10)
        assert resp.status_code == 200
        # 阅读页面应该有章节内容
        page_text = resp.text
        assert len(page_text) > 1000  # 页面应该有内容
