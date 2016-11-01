#coding:utf-8

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class Login(Page):
    '''
    用户登录页面
    '''
    url = '/'
    bbs_login_user_loc = (By.XPATH,".//*[@id='mzCust']/div/div[1]/img[1]")
    bbs_login_button_loc = (By.ID,"mzLogin")


    def bbs_login(self):
        #self.find_element(*self.bbs_login_user_loc).click()
        above = self.find_element(*self.bbs_login_user_loc)
        ActionChains(self.driver).move_to_element(above).perform()
        self.find_element(*self.bbs_login_button_loc).click()

    login_username_loc = (By.ID,"account")
    login_password_loc = (By.ID,"password")
    login_button_loc = (By.ID,"login")

    #登陆用户名

    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)

    #登录密码

    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)


    #登录按钮

    def login_botton(self):
        self.find_element(*self.login_button_loc).click()


    #定义统一的登录入口

    def user_login(self,username="username",password="1111"):
        """获取的用户名登录"""
        self.open()
        self.bbs_login()
        self.login_username(username)
        self.login_password(password)
        self.login_botton()
        sleep(1)

    #登录断言
    username_erro_loc = (By.XPATH,"//span[@for='account']")
    password_erro_loc = (By.XPATH,"//span[@for='password']")

    #用户名错误
    def username_erro(self):
        return self.find_element(*self.username_erro_loc).text

    #密码错误
    def password_erro(self):
        return self.find_element(*self.password_erro_loc).text

    #登录成功
















