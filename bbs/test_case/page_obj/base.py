#coding:utf-8

class Page(object):
    '''
    基础页面，供所有的页面对象继承
    '''
    bbs_url = "http://10.200.12.8:8099"
    def __init__(self,selenium_driver,base_url=bbs_url,parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def open(self):
        self._open(self.url)


    def script(self,src):
        self.driver.execute_script(src)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    #获取弹出框内的文案
    def alert_info(self):
        return self.driver.switch_to_alert()









