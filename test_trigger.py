"""
测试触发器 - 把这个文件放到服务器上的 Flask 项目里
然后在主 app.py 中添加: from test_trigger import test_bp
                           app.register_blueprint(test_bp)
"""
import subprocess
import os
from flask import Blueprint, render_template_string

test_bp = Blueprint("test", __name__, url_prefix="/test")

# 测试项目路径（服务器上的实际路径）
TEST_PROJECT_DIR = "/home/你的用户名/pytest_demo"
REPORT_DIR = os.path.join(TEST_PROJECT_DIR, "report")

INDEX_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>测试控制台</title>
</head>
<body>
    <h1>自动化测试控制台</h1>
    <form method="post" action="/test/run">
        <button type="submit">运行测试</button>
    </form>
    <br>
    <a href="/test/report">查看最新测试报告</a>
    <br><br>
    <pre>{{ output }}</pre>
</body>
</html>
"""

@test_bp.route("/", methods=["GET"])
def index():
    return render_template_string(INDEX_HTML, output="")

@test_bp.route("/run", methods=["POST"])
def run_tests():
    """运行测试并返回结果"""
    os.makedirs(REPORT_DIR, exist_ok=True)
    
    result = subprocess.run(
        ["pytest", "tests/", "-v", f"--html={REPORT_DIR}/report.html", "--self-contained-html"],
        cwd=TEST_PROJECT_DIR,
        capture_output=True, text=True, timeout=120
    )
    
    output = result.stdout + result.stderr
    return render_template_string(INDEX_HTML, output=output)

@test_bp.route("/report")
def view_report():
    """查看测试报告"""
    report_path = os.path.join(REPORT_DIR, "report.html")
    if os.path.exists(report_path):
        return open(report_path, encoding="utf-8").read()
    return "报告尚未生成，请先运行测试。"
