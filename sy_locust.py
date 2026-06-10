# Locust 性能测试笔记

# 安装
# pip install locust

# 基本用法
# 在终端运行（headless 无界面模式）：
# locust --headless -u 10 -r 2 --run-time 30s --host https://yileila.top
#   -u 10       模拟10个用户
#   -r 2        每秒启动2个用户
#   --run-time 30s  运行30秒
#   --host      目标网站地址

# 有 Web 界面的模式（浏览器访问 http://localhost:8089）：
# locust --host https://yileila.top

# 脚本结构
# from locust import HttpUser, task, between
# 
# class 用户类名(HttpUser):
#     wait_time = between(1, 3)  # 每个操作间隔1-3秒
#     
#     @task(权重数字)
#     def 任务名(self):
#         self.client.get("/路径")
#         self.client.post("/路径", json={})
# 
# 权重越大执行频率越高，@task(3) 比 @task(1) 多执行3次

# 检查响应
# with self.client.get("/路径", catch_response=True) as resp:
#     if resp.status_code == 200:
#         resp.success()
#     else:
#         resp.failure(f"状态码: {resp.status_code}")

# 常用参数
# 用户启动：       -u 10
# 启动速度：       -r 2
# 运行时间：       --run-time 30s
# 无界面模式：     --headless
# CSV 导出报告：  --csv=result

# 输出结果解读
# Type     请求方法
# Name     接口路径
# # reqs   请求总数
# # fails  失败数
# Avg      平均响应时间(ms)
# Min      最小响应时间(ms)
# Max      最大响应时间(ms)
# Med      中位数响应时间(ms)
# req/s    每秒请求数

# 对比 Jmeter（Java）
# Locust 用 Python 写脚本，轻量
# Jmeter 用 GUI 配，要装 Java
# 面试问性能测试，Locust 够用
