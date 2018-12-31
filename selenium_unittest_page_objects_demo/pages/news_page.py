from page_objects import PageObject, PageElement


class Baidu_news_Page(PageObject):
    search_input = PageElement(css='#ww', time_out=2)
    search_button = PageElement(css='#s_btn_wr', time_out=5)