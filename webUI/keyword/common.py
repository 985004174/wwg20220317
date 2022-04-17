# /Users/kevin.wu/PycharmProjects python
# -*- coding: utf-8 -*-
# author： kevin.wu
# datetime： 2022/4/14 12:11 PM 
# ide： PyCharm
import time

from selenium import webdriver

# 定义driver对象
# driver=webdriver.Chrome()
# driver.get('http://39.98.138.157/shopxo/index.php')
# driver.maximize_window()

# 定位元素
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from log.logger_config import test2_log


def open_browser(type_):
    if type_ == 'Chrome':
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        # print(type(driver))
    else:
        try:
            driver = getattr(webdriver, type_)()
        #     driver = webdriver.type_()
        except Exception as e:
            driver = webdriver.Chrome()
            print('异常信息：{}'.format(e))

    return driver









class Common:
    # 默认chorme为浏览器
    def __init__(self,type_):
        if type_ == 'Chrome':
            self.driver = open_browser(type_)



    def open(self, url):
        self.driver.get(url)

    # 定位元素
    def locate(self, name, value):
        return self.driver.find_element(name, value)

    # el = driver.find_element()
    # el().click()

    # 点击操作
    def click(self, name, value):
        self.locate(name, value).click()

    # 输入
    def input(self, name, value, txt):
        self.locate(name, value).send_keys(txt)

    # 退出
    def quit(self):
        self.driver.quit()

    # 显式等待
    def wait(self, name, value):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locate(name, value), message='元素查找失败')

    # 隐式等待
    def implict_wait(self, time_):
        self.driver.implicitly_wait(time_)

    # 强制等待
    def wait_sleep(self, time_):
        time.sleep(time_)

    # 切换句柄
    def change_handles(self, value):
        # 获取当前所有的句柄handles
        handles = self.driver.window_handles()
        #     此时handles返回一个list列表，我们用索引去切换句柄页
        self.driver.switch_to.window([handles])

    # 切换内嵌页面iframe
    def switch_frame(self, name, value):
        self.driver.switch_to.frame(self.locate(name, value))

    #   浏览器最大化
    # @pytest.mark.skip()
    def max_browser(self):
        self.driver.maximize_window()


    def get_text(self,name,value):
        return self.locate(name,value).text

    # 元素定位，传参list
    def locator_list(self):
        el = self.driver.find_element(list[0], list[1])

    #     切换default窗体
    def switch_default(self):
        self.driver.switch_to.default_content()


    # 切换浏览器句柄
    def switch_handle(value):
        driver = webdriver.Chrome()
        handels=driver.window_handles
        handles = driver.window_handles()(value)
        # 句柄 = 具柄列表[索引]
        # switch_handle(value)
        driver.switch_to.window([driver.window_handles()(value)])


    # 浏览器刷新
    def refresh(self):
        self.driver.refresh()


    # 判断元素是否存在
    def is_element_exist(self, name, value):

        el = self.locate(name, value)
        # 方法复用
        # ss=self.driver.find_element(name,value)
        if len(el) > 0:
            print('当前元素已存在')
        else:
            print('元素查找失败，请重新定位')


    # 鼠标悬停
    def Action_Chain(self, name, value):
        # 定位到需要悬停的元素
        # el = self.driver.find_element(name, value)
        # 悬停
        ActionChains(self.driver).move_to_element(self.locate(name, value)).perform()


    def log(self):
        self.log=test2_log()





if __name__ == '__main__':
    Common('Chrome')
    # Common.open('Cc')
