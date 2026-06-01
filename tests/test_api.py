import pytest
import requests
import json
from pathlib import Path
test_data_path = Path(__file__).parent.parent / "utilities" / "test_data.json"
LOGIN_CASES = json.load(open(test_data_path, encoding="utf-8"))
@pytest.mark.skip(reason="API接口未打开，暂时跳过")
@pytest.mark.api
class TestAPI:
    url = "http://127.0.0.1:5000"
 
    def test_api(self):
        """测试API接口"""
        response = requests.get(self.url)
        assert response.status_code == 200, f"预期状态码200，实际得到: {response.status_code}"

    @pytest.mark.parametrize("case", LOGIN_CASES)
    def test_create_article_via_api(self, case):
        """用API登录后发一篇文章"""
        import requests
        s = requests.Session()
        if case['expect'] == 'success':
            s.post(self.url + "/api/login", json={"username": case['username'], "password": case['password']})
            resp = s.post(self.url + "/api/articles", json={"title": "Test Article", "content": "This is a test article."})
            assert resp.status_code == 201, f"预期状态码201，实际得到: {resp.status_code}"
            # 调API查文章列表，确认数据已写入
            resp2 = s.get(self.url + "/api/articles")
            articles = resp2.json()
            titles = [a["title"] for a in articles]
            assert "Test Article" in titles, "文章列表中应包含刚发布的文章"
        else:
            resp = s.post(self.url + "/api/login", json={"username": case['username'], "password": case['password']})
            assert resp.status_code == 401, f"预期状态码401，实际得到: {resp.status_code}"