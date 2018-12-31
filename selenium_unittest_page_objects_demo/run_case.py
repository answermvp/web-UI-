# -*- coding: utf-8 -*-
import unittest
import os,sys,time
import HTMLTestRunner

case_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'test_case')

def run_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py',top_level_dir=None)
    return discover

if __name__ == '__main__':
    #按照一定格式获取当前时间
    now = time.strftime('%m%d_%H%M') 
    #将当前时间加入到报告文件名称中
    filename = './test_report/' + 'test_report_' + now + '.html'
    #定义测试报告存放路径
    fp = open(filename,'wb')

    runner=HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title=u'测试报告',
                description=u'测试百度首页和百度新闻搜索功能'
        )
    runner.run(run_case())
    fp.close()