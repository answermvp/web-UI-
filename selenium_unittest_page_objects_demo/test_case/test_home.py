import unittest
import time
from selenium import webdriver
from pages.home_page import Baidu_Home_Page


class Home_test(unittest.TestCase):
    """
    测试百度首页
    """
    @classmethod
    def setUpClass(cls):
        """初始化"""
        cls.dr = webdriver.Chrome(r'C:\Python\Python37\Lib\site-packages\selenium\driver\chromedriver.exe')
        cls.dr.maximize_window()        
        cls.page = Baidu_Home_Page(cls.dr)
        cls.page.get('https://www.baidu.com')

    def setUp(self):
        print(__doc__)

    def search(self, search_word):
        """搜索"""
        self.page.search_input.clear()
        self.page.search_input.send_keys(search_word)
        self.page.search_button.click()
        time.sleep(3)
        title = self.dr.title
        return title 

    def test_search_1(self):
        """百度首页搜索关键字：test"""
        title = self.search('test')
        self.assertEqual(title, 'test_百度搜索') 

    def test_search_2(self):
        """百度首页搜索关键字：selenium"""
        title = self.search('selenium')
        self.assertEqual(title, 'selenium_百度搜索')

    def tearDown(self):
        print('一条用例执行完毕')
        
    @classmethod
    def tearDownClass(cls):
        """
        关闭浏览器
        """
        cls.dr.quit()

if __name__ == '__main__':
    unittest.main()