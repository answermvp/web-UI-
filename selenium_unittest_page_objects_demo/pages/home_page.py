from page_objects import PageObject, PageElement


class Baidu_Home_Page(PageObject):
    search_input = PageElement(css='#kw', time_out=2)
    search_button = PageElement(id_='su', time_out=5)
