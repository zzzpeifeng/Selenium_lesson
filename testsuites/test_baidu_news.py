import unittest

from pageobject.BaiduPage import BaiDuPage
from pageobject.BaiduPage_News import BaiduNewsPage

from framework.base_page import BasePage


class Baidu_News(unittest.TestCase):

    def setUp(self):
        bro = BasePage(self)
        self.driver = bro.open_browser()

    def test_BaiduNews(self):
        baidu = BaiDuPage(self.driver)
        baidu.new_click()
        baidu_news = BaiduNewsPage(self.driver)
        baidu_news.type_ww("python")
        baidu_news.framework_sleep(3)
        baidu_news.click_wr()
        baidu_news.framework_sleep(2)
        baidu_news.framework_quit()


if __name__ == '__main__':
    unittest.main()
