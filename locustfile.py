"""Locust 性能测试脚本
用法: locust -f locustfile.py --headless -u 10 -r 2 --run-time 10s
      -u 10      模拟10个用户
      -r 2       每秒启动2个用户
      --run-time 10s  运行10秒
"""
from locust import HttpUser, task, between
import random


class BookSearchUser(HttpUser):
    host = "https://yileila.top"  # 加这一行
    # 每个用户执行任务之间的等待时间（1-3秒）
    wait_time = between(1, 3)

    # 测试数据
    keywords = ["剑来", "凡人修仙传", "斗罗大陆", "雪中悍刀行", "全职高手"]

    def on_start(self):
        """每个用户启动时执行一次"""
        print(f"用户 {self} 开始测试")

    @task(3)
    def search_book(self):
        """搜索书籍（权重3，执行频率更高）"""
        keyword = random.choice(self.keywords)
        with self.client.get(
            f"https://yileila.top/flask/book/?q={keyword}",
            name="/flask/book/?q=[keyword]",
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure(f"状态码: {resp.status_code}")

    @task(1)
    def home_page(self):
        """访问首页（权重1）"""
        with self.client.get("https://yileila.top/flask/book/", catch_response=True) as resp:
            if resp.status_code != 200:
                resp.failure(f"首页状态码: {resp.status_code}")
