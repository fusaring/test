from selenium import webdriver
from selenium.webdriver.chrome.options import Options #用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service #用于设置谷歌浏览器驱动路径
from selenium.webdriver.common.by import By #用于定位元素
import time
def sz():
    # 创建设置浏览器对象
    q=Options()
    # q.add_argument('--no-sandbox') # 禁用沙盒模式(增加兼容性)
    q.add_experimental_option('detach',True) # 关闭浏览器后不自动退出
    a1=webdriver.Chrome(service=Service('chromedriver.exe'),options=q) # 创建谷歌浏览器对象
    a1.implicitly_wait(10)
    return a1

az=sz()    
# az.get('https://www.bilibili.com/') # 打开网页
az.get('https://www.baidu.com/') # 打开网页
# az.get('https://yileila.top/flask/book/')
# az.get('https://yileila.top/flask/wallpaper/')
# time.sleep(2) 
# az.close() # 退出标签页
# az.quit() # 退出浏览器并释放驱动
# az.maximize_window() # 最大化窗口
# az.minimize_window() # 最小化窗口
# az.set_window_position(200,100) # 设置窗口位置
# az.set_window_size(800,800) # 设置窗口大小
# az.get_screenshot_as_file('Selen/1.jpg') # 截图并保存为文件
# az.refresh() # 刷新当前页面

# 定位元素
# a1=az.find_element(By.ID,'kw')
# print(a1)
# a2=az.find_elements(By.ID,'kw')
# print(a2)
# a1.send_keys('selenium') # 输入文本
# time.sleep(2)
# a1.clear() # 清除文本
# a1.submit() # 提交表
# a3=az.find_element(By.ID,'su')
# a3.click() # 点击元素
# a1=az.find_element(By.NAME,'q')
# a1=az.find_element(By.CLASS_NAME,'form-controlme-2')
# a1=az.find_element(By.TAG_NAME,'div')
# az.find_element(By.LINK_TEXT,'番剧').click()
# az.find_element(By.PARTIAL_LINK_TEXT,'继续阅读').click()
# az.find_elements(By.CSS_SELECTOR,'input')[7].send_keys('aaa')
# az.find_element(By.XPATH,'//*[@id="s-top-left"]/a[1]').click()
# az.find_element(By.XPATH,'/html/body/div/div/div[1]/a[1]').click()
# time.sleep(3)
# az.close()
# XPATH 复制浏览器xpath 通过属性+路径定位 full xpath 复制完整路径
# xpath 属性定位 //标签[@属性=值] 模糊定位 //标签contains(@属性，部分值)或者contains(text(),部分词) 可以用and or
# CSS_SELECTOR 元素定位 可以通过#id .class 标签头 任意类型定位：['类型=值‘] [类型*=模糊值] ^开头值 $结尾值 类似于正则
# PARTIAL_LINK_TEXT模糊文本定位
# LINK_TEXT精准文本定位 通过a标签文本 找到链接
# TAG_NAME查找标签 重复标签过多 需要切片
# class值不能有空格 否者报错 class值重复的有很多 需要切片 class有的网站值是随机的
# a1.send_keys('剑来') # 输入文本
# a1.submit() # 提交表
# az.implicitly_wait(10) 元素隐性等待 多少秒找到元素立即执行代码 时间内没有找到就报错
# az.find_element(By.XPATH,'/html/body/div/div[3]/form/div[3]/input').send_keys('https://haowallpaper.com/link/common/file/previewFileImg/18891187734760832')
# az.find_element(By.XPATH,'//*[@id="localUploadGroup"]/label').send_keys(r"C:/Users/Fus/Pictures/Camera Roll/girl-4k.jpg")
# az.find_element(By.XPATH,'/html/body/div/div[3]/form/button').click()
az.find_element(By.CSS_SELECTOR,'#s-top-left > a:nth-child(1)').click()
handles=az.window_handles
# az.close()
az.switch_to.window(handles[-1])
# time.sleep(2)
az.close()
# az.implicitly_wait(10)
# az.find_element(By.CSS_SELECTOR,'#ww').send_keys('aaa')
# window_handles 获取所有句柄 
# switch_to.window() 切换到指定的句柄标签页
# alert 弹窗 switch_to.alert 切换到指定弹窗
# accept() 确定 dismiss() 取消 text 获取弹窗文本
# iframe嵌套页面
# 先获取iframe元素 a_frame=az.finde_element(By.XPATH,'...')
# 再进入iframe页面 az.switch_to.frame(a_frame)
# 退出iframe嵌套页面 az.switch_to.default_content()

# text 获取文本 is_displayed 判断元素是否可见 先获取元素
# text=az.find_element(By.CSS_SELECTOR,'#pane-news > div > ul > li.hdline1 > strong > a:nth-child(1)')
# print(text.text)
# print(text.is_displayed())

# back() 网页后退
# forward() 网页前进
az.switch_to.window(handles[0])
az.back()
time.sleep(2)
az.forward()
az.delete_all_cookies() # 删除所有cookie
az.get_cookies() # 获取所有cookie
az.execute_script('window.scrollTo(0,document.body.scrollHeight)') # 执行js代码 滚动到页面底部
强制等待 time.sleep(2)
隐式等待 implicitly_wait() 全局的通用的等待 只要找不到元素就等一会
显式等待 针对性的 条件化的等待 需要导入模块
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element=WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.ID,''))
)
element.click()
WebDriverWait(driver,10).until(EC.可见((By.ID,'')))
EC缩写自expected_condtions(预期条件) expected (预期) + conditions (条件)	
visibility_of_element_located 可见 visibility (可见性) located (被定位) 元素被定位后的可见状态
