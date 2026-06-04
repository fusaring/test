# 书籍搜索网站自动化测试

基于 Python + pytest + Selenium 的自动化测试项目，测试对象为 [书籍搜索网站](https://yileila.top/flask/book/)。

## 技术栈

- **pytest** — 测试框架（fixture、parametrize、HTML报告）
- **Selenium** — UI 自动化（Page Object 模式）
- **requests** — 接口测试
- **GitHub Actions** — CI/CD 自动运行测试

## 项目结构

```
├── tests/             # 测试用例
├── page/              # Page Object 封装
├── utilities/         # 测试数据（JSON）
├── conftest.py        # fixture 配置
└── .github/workflows/ # CI/CD 配置
```

## 运行测试

```bash
pip install -r requirements.txt
pytest tests/ -v --html=report.html
```

## 查看报告

每次提交代码后，GitHub Actions 自动运行测试并生成报告：
[https://fusaring.github.io/test/report.html](https://fusaring.github.io/test/report.html)

![CI](https://github.com/fusaring/test/actions/workflows/test.yml/badge.svg)
