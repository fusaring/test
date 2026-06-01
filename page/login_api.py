from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """博客登录页操作封装"""
    
    def __init__(self, driver):
        self.driver = driver
    
    # 元素定位
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    error_message = (By.ID, "message")
    
    def open(self):
        self.driver.get("http://127.0.0.1:5000/login")
    
    def input_username(self, text):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_input)
        ).send_keys(text)
    
    def input_password(self, text):
        self.driver.find_element(*self.password_input).send_keys(text)
    
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
    
    def login(self, username, password):
        """一键登录"""
        self.open()
        self.input_username(username)
        self.input_password(password)
        self.click_login()
    
    def get_error_text(self):
        return self.driver.find_element(*self.error_message).text
