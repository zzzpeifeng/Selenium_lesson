from selenium import webdriver

from framework.base_page import BasePage
from pageobject.BaiduPage import BaiDuPage
import unittest


class BaiduSerch(unittest.TestCase):

    def setUp(self):
        bro = BasePage(self)
        self.driver = bro.open_browser()

    def test_baisu(self):
        '''测试百度搜索'''
        baisu = BaiDuPage(self.driver)
        baisu.kw_send('selenium')
        baisu.su_click()




if __name__ == '__main__':
    unittest.main()
