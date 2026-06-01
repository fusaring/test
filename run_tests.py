import subprocess
import os

# 项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "report")

def run_tests():
    """运行测试"""
    os.makedirs(REPORT_DIR, exist_ok=True)
    
    result = subprocess.run(
        ["pytest", "tests/", "-v", f"--html={REPORT_DIR}/report.html", "--self-contained-html"],
        cwd=BASE_DIR,
        capture_output=True,
        text=True
    )
    
    return {
        "success": result.returncode == 0,
        "output": result.stdout + result.stderr,
        "returncode": result.returncode
    }

if __name__ == "__main__":
    result = run_tests()
    print(result["output"])
