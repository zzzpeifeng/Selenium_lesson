from framework.base_page import BasePage

class BaiduNewsPage(BasePage):

    ww = ('id','ww')
    wr = ('id','s_btn_wr')

    def type_ww(self,value):
        self.send(self.ww,value)

    def click_wr(self):
        self.click(self.wr)
