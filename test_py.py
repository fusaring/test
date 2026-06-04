# 创建用例
# 文件以test_开头，结尾以.py结尾
# 文件内容以test_开头，结尾以.py结尾 

# 执行用例
# 在代码根目录外文件夹建立一个tests文件夹，在该文件夹下执行pytest命令，pytest会自动识别以test_开头的文件，并执行其中以test_开头的函数。

# 执行结果 
# 成功 passed . 失败 failed F 跳过 skipped s 出错 error E 预期失败 expected failure x 预期成功 unexpected success X

# 用例发现规则
# 遍历所有目录 venv和.开头的文件夹除外，找到以test_开头的文件，执行其中以test_开头的函数。
# 遍历所有py文件，找到以test_开头或以_test结尾的函数，执行这些函数。
# 遍历所有test的类 pytest 会尝试调用类的无参构造函数，如果定义了 __init__(self, something) 会导致错误。最佳实践是不要定义 __init__，改用 setup_method 或 fixture。
# 收集符合要求的函数、方法，test_开头 没有参数的函数，执行这些函数。

# pytest进阶管理 
# 配置
#  配置的目的是了更好地管理测试用例，pytest提供了一个配置文件pytest.ini，可以在其中设置一些全局的配置项，例如测试用例的路径、测试报告的格式等。
    # addopts 设置运行pytest时的默认命令行参数 addopts = -v -s --tb=short --strict-markers -v: 输出详细信息；-s: 允许print打印；--tb=short: 精简报错信息；--strict-markers: 强制所有mark标记都已注册，防止拼写错误
    # testpaths 	指定 pytest 递归搜索测试用例的根目录 testpaths = tests 多个目录要分行 指定后，运行pytest时会在此目录下查找，可显著提升测试发现速度
    # python_files 自定义测试文件的命名规则 python_files = test_*.py check_*.py 默认只匹配test_*.py和*_test.py，此处扩展为也匹配以check_开头的文件
    # python_classes 自定义测试类的命名规则 python_classes = Test* Check* 除了默认的Test开头，也可以匹配以Check开头的类
    # python_functions 自定义测试方法/函数的命名规则 python_functions = test_* check_* 除了默认的test_开头，也可以匹配以check_开头的函数
    # markers 注册自定义标记，实现用例分组，并可添加说明 markers = <br> smoke: 核心冒烟测试用例 <br> login: 登录模块相关测试 <br> slow: 执行缓慢的测试（超过2秒）
    # 注册后可避免因拼写错误（如 smoke 误写成 somke）导致静默失败，且运行 pytest --markers 可查看所有注册标记的说明
    # norecursedirs 排除某些目录，避免 pytest 进入搜索 norecursedirs = .* venv env logs results 可大幅提升测试发现的速度


# 命令参数
#     -h 显示帮助信息
#     -x 遇到第一个失败的测试用例就停止执行
#     -v 显示详细信息
#     -k 只运行指定的测试用例
#     -s 显示测试用例的输出信息
#     -m 只运行标记了指定标签的测试用例
#     --lf (--last-failed)	只运行上次失败的用例
#     --ff (--failed-first)	先运行上次失败的用例，再运行其余
#     --maxfail=N	遇到 N 个失败后停止
#     --collect-only	仅收集并显示测试用例，不执行
#     -q (--quiet)	简化输出，适合 CI
#     --tb=short / --tb=no	控制回溯信息的详细程度 short 只显示失败的行 no 不显示回溯信息

# gvsi-tts .\runtime\python api_v2.py

# fixtures
    # 功能 前、后置操作，数据准备和清理，资源管理，参数化测试等
    # 基本语法 使用 @pytest.fixture 装饰一个函数，该函数返回测试所需的资源（比如 WebDriver 对象）。测试函数通过参数名来请求使用这个 fixture。
    # pytest 会自动发现名为 browser 的 fixture，并将它的返回值注入到测试函数中。
    # 每个测试函数调用时，fixture 都会重新执行（默认作用域是 function）。
    # 可以在 fixture 中使用 yield 来分离“准备”和“清理”代码：yield 之前的代码在测试前执行，yield 之后的代码在测试后执行。
    # fixture 的作用域（scope）
        # function（默认）	每个测试函数调用一次
        # class	每个测试类执行一次（所有类中的方法共享）
        # module	每个 .py 文件执行一次
        # session	整个 pytest 运行会话只执行一次（适合全局浏览器实例）
        # package    每个包执行一次（适合跨模块共享的资源）
    # 当你多个测试文件都要使用同一个 fixture（比如 browser），可以把它放到项目根目录或测试目录下的 conftest.py 文件中。pytest 会自动发现该文件中的 fixture，无需手动导入。
    # 每个目录中的 conftest.py 只对该目录及其子目录中的测试文件生效。子目录的 conftest.py 会覆盖或扩展父目录的 fixture 和钩子,同名 fixture 会被子目录的覆盖，但不同名的会合并。
    # fixture 之间可以互相依赖  一个 fixture 可以请求另一个 fixture，实现更复杂的准备逻辑。例如，先登录获取 token，再传给下游
    # 参数化 fixture（间接参数化） 有时希望同一个 fixture 能返回不同的配置（例如不同的浏览器类型）。pytest 提供 @pytest.fixture(params=[...]) 语法，fixture 会依次返回每个参数值，每个值会生成一个测试。
    # request.param：当 fixture 使用了 params 参数时，request.param 就是当前这次执行所对应的那个参数值。
    # 自动使用 fixture（autouse）如果你希望某个 fixture 在每一个测试前自动执行（比如清理缓存、设置环境变量），而无需在测试参数中显式请求，可以设置 autouse=True。
    # pytest fixture 中的 request
        # request 是 pytest 内置的一个特殊 fixture，它代表“当前测试请求的上下文”。当你在自定义 fixture 的参数中写上 request，pytest 会自动注入这个对象。
        # request.param：当 fixture 使用了 params 参数时，request.param 就是当前这次执行所对应的那个参数值。
        # request.node：当前测试用例的节点对象，可以获取测试名称、标记、文件位置等。request.node.get_closest_marker("keep_cookies") 获取测试用例标签名
        # request.config：获取 pytest 配置（如命令行参数）
        # request.fixturename：当前 fixture 的名称
    # 内置的实用 Fixture
        # tmp_path —— 临时目录，每个测试函数都会得到一个独立的临时目录，测试结束后会自动删除。
        # def test_save(tmp_path):              # 参数名固定叫 tmp_path
        #     file = tmp_path / "myfile.txt"    # 在临时文件夹里创建文件
        #     file.write_text("hello")
        #     assert file.read_text() == "hello"
        # capsys —— 捕获标准输出/错误 captured.out 是标准输出，captured.err 是错误输出。
        # def test_print(capsys):
        #     print("Hello, pytest!")
        #     captured = capsys.readouterr()       # 捕获输出
        #     assert captured.out == "Hello, pytest!\n"
        # caplog —— 捕获日志
        # def test_logger(caplog):
        #     caplog.set_level(logging.INFO)          # 设置监听级别
        #     logging.info("User login")
        #     assert "User login" in caplog.text      # caplog.text 是所有日志文本
        #     assert caplog.records[0].levelname == "INFO"
        # monkeypatch —— 动态修改属性/环境变量
        # def test_mode(monkeypatch):
        #     monkeypatch.setenv("MODE", "test")
        #     assert os.getenv("MODE") == "test"
        #      测试结束，环境变量自动恢复原状
# mark
    # 功能 用于给测试用例打标签，实现分组管理和选择性执行
    # 基本语法 使用 @pytest.mark.标签名 来标记测试函数或类。例如，@pytest.mark.smoke 标记冒烟测试。
    # 运行时选择标签 通过 pytest -m "标签名" 来运行特定标签的测试用例。例如，pytest -m "smoke" 只运行标记了 smoke 的测试。
    # 多标签组合 可以使用逻辑表达式组合多个标签，例如 pytest -m "smoke and not login" 运行标记了 smoke 但没有 login 的测试。
    # 标签注册 在 pytest.ini 中注册自定义标签，可以添加说明，避免拼写错误导致静默失败。markers = <br> smoke: 核心冒烟测试用例 <br> login: 登录模块相关测试 <br> slow: 执行缓慢的测试（超过2秒）
    # @pytest.mark.parametrize 参数化测试 用于多组数据驱动一个测试逻辑
    # @pytest.mark.skip(reason="暂时不跑") 无条件跳过
    # @pytest.mark.skipif(sys.platform == "win32", reason="条件满足时跳过") 条件跳过
    # @pytest.mark.xfail(reason="预期失败的测试用例") 运行结果会显示 XFAIL（预期失败），不破坏整体测试结果。

# 断言异常（pytest.raises）用于断言代码是否抛出了预期的异常。
def test_bad_input():
    with pytest.raises(ValueError, match="用户名不能为空"):
        login("")

# 常用插件
    # pytest-html：生成直观的HTML测试报告，便于结果可视化与分享 pytest --html=report.html 或写在pytest.ini中 addopts = --html=report.html
    # pytest-cov：测量代码覆盖率，以此优化测试用例  pytest --cov=your_package
    # pytest-xdist：实现测试的并行执行，显著缩短测试时间 pytest -n auto
    # pytest-rerunfailures：自动重试失败的用例，常用于处理网络波动等不稳定因素 pytest --reruns 3
    # pytest-timeout：为测试用例设置超时时间，避免单个用例卡死导致整个测试流程挂起  pytest --timeout=5
    # allure-pytest：生成更高级的可视化报告，支持分类、图表等，比HTML报告更专业 
    # pytest-sugar：改善终端输出的样式，增加进度条，让测试运行状态更一目了然    
    # pytest-instafail：在测试失败时立即显示失败信息，而不是等到整个测试套件运行完毕    

# 截图部分
# 把 pytest_runtest_makereport 理解成一个监听器。pytest 在执行每个测试的每个阶段（setup、call、teardown）都会自动调用这个函数，并告诉你当前阶段的结果（成功/失败/跳过）
# 需要在阶段是 call（真正的测试函数运行阶段）并且结果是失败的时候，执行截图逻辑 调用 driver.get_screenshot_as_base64() 截图，然后交给 pytest-html 插件显示
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
#     @pytest.hookimpl 是 pytest 用来注册钩子函数的装饰器。
#     tryfirst=True：表示这个钩子要尽量早地执行（在其他钩子之前） 
#     hookwrapper=True：表示这个钩子是一个“包装器”，可以拦截测试执行的前后过程（类似 yield 的 setup/teardown）。
#     pytest_runtest_makereport 是 pytest 内置的一个钩子名称，pytest 在执行测试的每个阶段（setup/call/teardown）时都会自动调用它。函数在call阶段就已经执行完毕 teardown是清理阶段执行关闭浏览器 清空缓存等
#     yield 不仅能够向外产出值（就像在 fixture 中那样），还能从调用方接收值（通过 outcome = yield 的形式）。这通常需要配合装饰器和生成器的 send() 方法，但 pytest 封装好了，

import pytest
from selenium import webdriver
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver            # 把 driver 提供给测试函数
    driver.quit()           # 测试结束后执行清理
def test_search(browser):
    pass
@pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
def test_search(browser):
    pass
def test_02():
    assert 1 == 2
