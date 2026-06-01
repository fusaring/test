import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestWindowAndAlert:

    def test_window_switch(self, browser):
        """窗口切换"""
        browser.get("https://www.baidu.com")

        # 1. 获取当前窗口句柄
        main_window = browser.current_window_handle
        print(f"主窗口句柄: {main_window}")

        # 2. 点击一个会打开新窗口的链接
        browser.find_element(By.LINK_TEXT, "新闻").click()

        # 3. 获取所有窗口句柄
        all_handles = browser.window_handles
        print(f"所有窗口: {all_handles}")

        # 4. 切换到新窗口（最后一个）
        browser.switch_to.window(all_handles[-1])
        print(f"当前标题: {browser.title}")

        # 5. 切回主窗口
        browser.switch_to.window(main_window)
        print(f"切回后标题: {browser.title}")

    def test_alert_accept(self, browser):
        """弹窗 — 确定"""
        browser.get("https://www.baidu.com")

        # 用 JS 弹一个 alert
        browser.execute_script("alert('这是一个弹窗')")
        time.sleep(1)

        # 切换到弹窗并点击确定
        alert = browser.switch_to.alert
        print(f"弹窗文字: {alert.text}")
        alert.accept()  # 确定

    def test_alert_dismiss(self, browser):
        """弹窗 — 取消"""
        browser.get("https://www.baidu.com")

        # 用 JS 弹一个 confirm
        browser.execute_script("confirm('确定要删除吗？')")
        time.sleep(1)

        alert = browser.switch_to.alert
        print(f"弹窗文字: {alert.text}")
        alert.dismiss()  # 取消

    def test_alert_input(self, browser):
        """弹窗 — 输入文本"""
        browser.get("https://www.baidu.com")

        # 用 JS 弹一个 prompt
        browser.execute_script("prompt('请输入你的名字：')")
        time.sleep(1)

        alert = browser.switch_to.alert
        alert.send_keys("柒")  # 输入文本
        alert.accept()  # 确定
