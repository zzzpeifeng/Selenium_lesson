import HTMLTestRunnerCN
import os

import getcwd
import testsuites.test_baidu
import testsuites.test_baidu_news
import unittest

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(testsuites.test_baidu.BaiduSerch('test_baisu'))
    suite.addTest(testsuites.test_baidu_news.Baidu_News('test_BaiduNews'))

    path = getcwd.getcwd()

    file_path = os.path.join(path,'Report/UI测试用例报告.html')

    fp = open(file_path,'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(stream = fp,title = 'xxxUI自动化测试报告',description = '报告中描述部分',tester = '测试者')

    runner.run(suite)
    fp.close()