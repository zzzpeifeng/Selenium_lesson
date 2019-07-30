from framework.base_page import BasePage


class BaiDuPage(BasePage):
    kw = ('id', 'kw')  # 定位搜索输入框
    su = ('id', 'su')  # 搜索按钮
    new = ('link','新闻') # 新闻链接

    def kw_send(self, value):  # 搜索框输入内容
        self.send(self.kw, value)

    def su_click(self):  # 点击搜索按钮
        self.click(self.su)

    def new_click(self):
        self.click(self.new)
