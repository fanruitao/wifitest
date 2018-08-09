#coding=utf-8
from webpage.BasePage import BasePage
from  common.commonconfig import base_url,right_password
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):
    """登录页面"""
    passwordinputbox=('id','admin_Password1')
    loginbutton=('id','logIn_btn')
    internetset=('xpath',"//div[@id='want_internet_id']/div/span")
    errorinfo=('id','errorinfo_1')


    def __init__(self,browser = 'chrome'):
        super().__init__(browser)

    def input_password(self,rightpassword):
        password=self.findElement(self.passwordinputbox)
        self.type(password,rightpassword)
    def click_login(self):
        loginbutton=self.findElement(self.loginbutton)
        self.click(loginbutton)
    def error_info_displayed(self):
        errorinfo=self.findElement(self.errorinfo)
        return self.elementdisplay(errorinfo)
    def error_info_text(self):
        errorinfo = self.findElement(self.errorinfo)
        return self.getText(errorinfo)
















