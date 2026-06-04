from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchBook:
    def __init__(self, driver):
        self.driver = driver
    
    # 元素定位
    search_input = (By.NAME, "q")
    search_button = (By.XPATH, "/html/body/div/div/div[1]/div/form/button")

    def open(self):
        self.driver.get("https://yileila.top/flask/book/")
        self.driver.implicitly_wait(10)  # 隐式等待，最长等待10秒，直到元素出现
    def input_search(self, text):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_input)
        )
        search_input.clear()  # 先清空
        search_input.send_keys(text)
    def click_search(self):
        self.driver.find_element(*self.search_button).click()
    # def add_to_cart(self):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.text_to_be_present_in_element((By.CLASS_NAME, "btn btn-sm btn-success"), "添加到书架")
    #     ).click()
    def search(self, keyword):
        """一键搜索"""
        self.open()
        self.input_search(keyword)
        self.click_search()
        # self.add_to_cart()
    def a_link(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "📖 继续阅读"))
        ).click()
    def a_link_partial(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "继续阅读").click()