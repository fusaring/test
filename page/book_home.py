from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BookHomePage:
    """图书首页 Page Object"""

    def __init__(self, driver):
        self.driver = driver

    # 元素定位
    search_input = (By.NAME, "q")
    search_button = (By.XPATH, "//button[@type='submit']")
    book_cards = (By.CLASS_NAME, "card-title")
    read_links = (By.PARTIAL_LINK_TEXT, "继续阅读")

    def open(self):
        self.driver.get("https://yileila.top/flask/book/")

    def get_title(self):
        return self.driver.title

    def search(self, keyword):
        """搜索书籍"""
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_input)
        )
        search_box.clear()
        search_box.send_keys(keyword)
        self.driver.find_element(*self.search_button).click()
        # 等搜索结果加载
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), keyword[:2]))

    def get_book_names(self):
        """获取当前页面显示的所有书名"""
        cards = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.book_cards)
        )
        return [card.text for card in cards]

    def click_first_read(self):
        """点击第一个'继续阅读'链接"""
        read_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.read_links)
        )
        read_link.click()

    def get_search_input_value(self):
        """获取搜索框当前值"""
        return self.driver.find_element(*self.search_input).get_attribute("value")
