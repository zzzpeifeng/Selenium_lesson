from selenium import webdriver
from framework.base_page import  BasePage

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

s = driver.window_handles

b_driver = BasePage(driver)
kw = ('id','kw')

b_driver.send(kw,'富璟科技')
b_driver.framework_sleep(3)
b_driver.send(kw,"凯捷中国")

su = ('id','su')

b_driver.click(su)
b_driver.get_img()
b_driver.framework_sleep(2)
b_driver.framework_quit()
