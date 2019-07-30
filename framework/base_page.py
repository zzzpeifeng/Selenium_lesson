import os
import time
import configparser
import getcwd
from logs.log import log1
from selenium import webdriver

path = getcwd.getcwd()
config_path = os.path.join(path, 'Config/config.ini')
config = configparser.ConfigParser()
config.read(config_path, encoding="utf-8-sig")

class BasePage(object):
    """
        framework 包下存放一些公共类
        测试基类
    """

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def is_displayed(element):
        """判断元素是否存在"""
        value = element.is_displayed()
        return value

    @staticmethod
    def framework_sleep(secondes):
        """"强制等待"""
        time.sleep(secondes)
        log1.info("暂停%d秒" % secondes)

    def get_img(self):
        """截图"""
        path = os.path.join(getcwd.getcwd(), 'screenshots\\')  # 拼接截图保存路径
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 按格式获取当前时间
        screen_name = path + rq + '.png'  # 拼接截图名称
        try:
            self.driver.get_screenshot_as_file(screen_name)
            log1.info("截图成功：%s" % screen_name)
        except BaseException:
            log1.error("截图失败：%s" % screen_name)

    def find_element(self, selector):
        by = selector[0]
        value = selector[1]
        element = None
        if by == 'id' or by == 'name' or by == 'class' or by == 'tag' or by == 'link' or by == 'plink' or by == 'css' or by == 'xpath':
            if by == 'id':
                element = self.driver.find_element_by_id(value)
            elif by == 'name':
                element = self.driver.find_element_by_name(value)
            elif by == 'class':
                element = self.driver.find_element_by_class_name(value)
            elif by == 'tag':
                element = self.driver.find_element_by_tag_name(value)
            elif by == 'link':
                element = self.driver.find_element_by_link_text(value)
            elif by == 'plink':
                element = self.driver.find_element_by_partial_link_text(value)
            elif by == 'css':
                element = self.driver.find_element_by_css_selector(value)
            elif by == 'xpath':
                element = self.driver.find_element_by_xpath(value)
            else:
                log1.error('没有找到元素')
            return element
        else:
            log1.error("输入的元素定位方式错误")

    def send(self, selector, value):
        element = self.find_element(selector)  # 调用封装的定位元素方法
        element.clear()

        try:
            element.send_keys(value)
            log1.info('输入的内容%s' % value)
        except BaseException:
            log1.error('输入内容出错')
            self.get_img()

    def click(self, selector):
        element = self.find_element(selector)

        try:
            element.click()
        except BaseException:
            display = self.is_displayed(element)
            if display:
                self.framework_sleep(3)
                element.click()
            else:
                self.get_img()
                log1.error("点击元素错误")

    def use_js(self, js):
        """调用js"""
        try:
            self.driver.execute_script(js)

        except BaseException:
            log1.error("js执行错误")

    def switch_menue(self, parent_element, seconds_element, target_element):
        """三级菜单切换"""
        self.framework_sleep(2)
        try:
            self.driver.switch_to_default_content()
            self.click(parent_element)
            log1.info("成功点击第一级菜单")
            self.click(seconds_element)
            log1.info("成功点击第二级菜单")
            self.click(target_element)
            log1.info("成功点击第三级菜单")
        except:
            log1.info("切换菜单报错")

    def switch_iframe(self, selector):
        """切换frame"""
        element = self.driver.find_element(selector)

        try:
            self.driver.switch_to.frame(element)
        except:
            log1.error("切换frame报错")

    def get_title(self):
        """获取title"""
        title = self.driver.title
        log1.info("当前窗口的title是%s" % title)
        return title

    def framework_quit(self):
        self.driver.quit()
        log1.info("关闭浏览器")

    def config_get(self, key, section=None):
        """读取配置文件字段的值并返回"""
        switch = config.get('environment', 'switch')
        if section == None and switch == str(0):
            section = 'test'
        elif section == None and switch == str(1):
            section = 'prod'
        config_get = config.get(section, key)
        return config_get

    def config_write(self, key=None, value=None, section=None):
        """往配置文件写入键值"""
        switch = config.get('environment', 'switch')
        if section == None and switch == str(0):
            section = 'test'
        elif section == None and switch == str(1):
            section = 'prod'
        if key is not None and value is not None:
            config.set(section, key, value)
            log1.info('在section:%s下写入%s=%s' % (section, key, value))
            with open(config_path, 'w', encoding='utf-8')as f:
                config.write(f)
        else:
            config.add_section(section)
            log1.info('新增section：%s' % section)
            with open(config_path, 'w', encoding='utf-8')as f:
                config.write(f)

    def config_delete(self, key=None, section=None):
        '''删除配置文件字段'''
        switch = config.get('environment', 'switch')
        if section == None and switch == str(0):
            section = 'test'
        elif section == None and switch == str(1):
            section = 'prod'
        if key is not None:
            config.remove_option(section, key)
            log1.info('删除section:%s下key为：%s的记录' % (section, key))
            with open(config_path, 'w', encoding='utf-8')as f:
                config.write(f)
        else:
            config.remove_section(section)
            log1.info('删除section:%s' % section)
            with open(config_path, 'w', encoding='utf-8')as f:
                config.write(f)

    def open_browser(self):
        browser = self.config_get('browser', 'environment')
        log1.info('读取浏览器配置')
        url = self.config_get('url')
        log1.info('读取url：%s' % url)
        try:
            if browser == str(0):
                self.driver = webdriver.Chrome()
                log1.info('打开的浏览器为Chrome')
            elif browser == str(1):
                self.driver = webdriver.Firefox()
                log1.info('打开的浏览器为Firefox')
            self.driver.get(url)
            self.driver.maximize_window()
            log1.info('浏览器最大化')
            self.driver.implicitly_wait(10)
            log1.info('设置静态等待时间10秒')
            return self.driver
        except BaseException:
            log1.error('浏览器打开报错')
