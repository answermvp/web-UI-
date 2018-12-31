import unittest
import time
from selenium import webdriver
from pages.news_page import Baidu_news_Page
from pages.home_page import Baidu_Home_Page


class News_test(unittest.TestCase):
    """
    测试百度新闻
    """
    @classmethod
    def setUpClass(cls):
        """初始化"""
        cls.dr = webdriver.Chrome(r'C:\Python\Python37\Lib\site-packages\selenium\driver\chromedriver.exe')
        cls.dr.maximize_window()        
        cls.news_page = Baidu_news_Page(cls.dr)
        cls.home_page = Baidu_Home_Page(cls.dr)
        cls.news_page.get('http://news.baidu.com/')

    def setUp(self):
        print(__doc__)

    def news_search(self, search_word):
        """搜索"""
        self.news_page.search_input.clear()
        self.news_page.search_input.send_keys(search_word)
        self.news_page.search_button.click()
        time.sleep(2)
        title = self.dr.title
        return title 

    def home_search(self, search_word):
        """搜索"""
        self.home_page.search_input.clear()
        self.home_page.search_input.send_keys(search_word)
        self.home_page.search_button.click()
        time.sleep(2)
        title = self.dr.title
        return title 

    def test_search_1(self):
        """百度新闻搜索关键字：test"""
        title = self.news_search('test')
        self.assertEqual(title, '百度新闻搜索_test') 

    def test_search_2(self):
        """百度新闻搜索关键字：selenium"""
        title = self.home_search('selenium')
        self.assertEqual(title, '百度新闻搜索_selenium')

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