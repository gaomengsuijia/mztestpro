#coding:utf-8
from time import sleep
import unittest,sys,random
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import Login
from time import sleep
from selenium.webdriver.common.by import By


class LoginTest(myunit.MyTest):
    '''社区登录'''

    #测试用户登录
    def user_login_verify(self,username="",password=""):
        Login(self.driver).user_login(username,password)

    def test_login1(self):
        '''用户名和密码都为空'''
        self.user_login_verify()
        po = Login(self.driver)
        username_mes = po.username_erro()
        password_mes = po.password_erro()
        print(username_mes)
        print(password_mes)
        self.assertEqual(username_mes,'账号不能为空')
        self.assertEqual(password_mes,'密码不能为空')
        sleep(2)
        function.insert_img(self.driver,'username_pass_kong.jpg')

    def test_login2(self):
        '''用户名正确，密码为空'''
        self.user_login_verify(username='18565660212')
        po = Login(self.driver)
        password_mes = po.password_erro()
        print(password_mes)
        self.assertEqual(password_mes,'密码不能为空')
        function.insert_img(self.driver, 'password_kong.jpg')







if __name__ == '__main__':
    unittest.main()
