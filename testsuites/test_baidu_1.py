from selenium import webdriver
from framework.base_page import BasePage
from logs.log import log1

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
s = driver.window_handles

kw = ('id', 'kw')

base_driver = BasePage(driver)
base_driver.send(kw, 'selenium+python')
base_driver.framework_sleep(2)

su = ('id', 'su')
base_driver.click(su)
base_driver.get_img()
base_driver.framework_sleep(3)

log1.info(base_driver.get_title())

base_driver.framework_quit()
