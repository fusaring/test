import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import json
from pathlib import Path
json_path = Path(__file__).parent / "utilities" / "test_book.json"
with open(json_path, encoding="utf-8") as f:
    BOOK_DATA = json.load(f)


@pytest.fixture(scope='session')
def browser():
    options = Options()

    # CI 环境（GitHub Actions）用无头模式
    if os.environ.get("CI"):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    else:
        options.add_experimental_option('detach', True)

    local_path = r'F:\Pys\chromedriver.exe'
    if os.path.exists(local_path):
        service = Service(local_path)
    else:
        from webdriver_manager.chrome import ChromeDriverManager
        service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()


@pytest.fixture
def sample_data():
    data = {"name": "辉夜", "level": 99, "title": "完美无瑕的大小姐"}
    print("\n[Fixture] 数据准备完成")
    yield data
    print("[Fixture] 数据清理完成")
    data.clear()


@pytest.fixture
def number_list():
    nums = [1, 2, 3, 4, 5]
    print("\n[Fixture] 数字列表准备好了")
    yield nums
    print("[Fixture] 数字列表已清理")
    nums.clear()
@pytest.fixture(params=BOOK_DATA)
def book_data(request):
    """参数化书籍数据"""
    print(f"\n[Fixture] 准备书籍数据: {request.param['keyword']}")
    yield request.param
    print(f"[Fixture] 书籍数据清理: {request.param['keyword']}")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser")
        if driver:
            from pytest_html import extras
            img = driver.get_screenshot_as_base64()
            extras_list = getattr(report, "extras", [])
            extras_list.append(extras.image(img, ""))
            report.extras = extras_list
            
            # 同时保存一份本地文件
            import os
            save_dir = os.path.join(os.path.dirname(__file__), "report", "screenshots")
            os.makedirs(save_dir, exist_ok=True)
            driver.save_screenshot(os.path.join(save_dir, f"{item.name}.png"))
