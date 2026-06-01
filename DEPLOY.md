# 部署到服务器步骤

## 1. 服务器上装依赖
```bash
# 安装 Python 依赖
pip install pytest selenium requests pytest-html webdriver-manager

# 安装 Chrome 浏览器
sudo apt update
sudo apt install -y google-chrome-stable

# 安装 ChromeDriver（或者用 webdriver-manager 自动管理）
```

## 2. 上传项目
把 `pytest_demo` 整个文件夹传到服务器上，比如放到：
```
/home/你的用户名/pytest_demo/
```

## 3. 配置 conftest.py
conftest.py 已经适配了 CI 环境（headless 无头模式），在 Linux 服务器上会自动使用无头浏览器，不需要显示器。

## 4. 集成到 Flask
在服务器 Flask 项目的 `app.py` 中添加：
```python
from test_trigger import test_bp
app.register_blueprint(test_bp)
```

## 5. 访问测试控制台
浏览器打开：
```
http://你的域名/test/
```
点"运行测试"按钮，等几秒就能看到结果。
测试报告在：`http://你的域名/test/report`
