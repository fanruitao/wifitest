from webpage.BasePage import BasePage
import time
from webpage.LoginPage import LoginPage
from  common.commonconfig import base_url,right_password

class LanPage(BasePage):
    passwordinputbox = ('id', 'admin_Password1')
    loginbutton = ('id', 'logIn_btn')
    more=('xpath',"//div[@id='want_more_id']/div")
    lanset=('id',"lang_dhcpsever")
    lanip=('id','lanIP')
    dhcpbutton=('id','dhcp_statue')
    dhcppool=('id','dhcppool')
    startip=('id','startLanIp')
    endip=('id','endLanIp')
    savebutton=('id','savebutton5')
    errorinfo=('id','errorinfo_1')
    popalert=("id","CreatePopAlertMessage")
    errorinfo2=("id","errorinfo_2")




    def __init__(self, browser='chrome'):
        super().__init__(browser)
        print(self.driver)


    def goto_lan(self):
        self.baseurl = base_url()
        self.rightpasword = right_password()
        self.open(self.baseurl)
        time.sleep(5)
        password = self.findElement(self.passwordinputbox)
        self.type(password, self.rightpasword)
        loginbox = self.findElement(self.loginbutton)
        self.click(loginbox)
        time.sleep(5)
        morebox = self.findElement(self.more)
        self.click(morebox)
        time.sleep(5)
        lanset=self.findElement(self.lanset)
        self.click(lanset)
    def get_lanip(self):
        lanip=self.findElement(self.lanip)
        return self.getAttribute(lanip,"value")
    def get_dhcpstatus(self):
        dhcpstatus=self.findElement(self.dhcpbutton)
        return self.getAttribute(dhcpstatus,"class")
    def get_startip(self):
        startip=self.findElement(self.startip)
        return self.getAttribute(startip,'value')
    def get_endip(self):
        endip=self.findElement(self.endip)
        return self.getAttribute(endip,'value')
    def set_lanip(self,value):
        lanip=self.findElement(self.lanip)
        self.type(lanip,value)
    def set_startip(self,value):
        startip = self.findElement(self.startip)
        self.type(startip,value)
    def set_endip(self,value):
        endip = self.findElement(self.endip)
        self.type(endip,value)
    def clear_lanip(self):
        lanip = self.findElement(self.lanip)
        self.clear(lanip)
    def clear_startip(self):
        startip=self.findElement(self.startip)
        self.clear(startip)
    def clear_endip(self):
        endip=self.findElement(self.endip)
        self.clear(endip)
    def click_savebutton(self):
        savebutton=self.findElement(self.savebutton)
        self.click(savebutton)
    def get_error_text(self):
        errorinfo=self.findElement(self.errorinfo)
        return self.getText(errorinfo)
    def get_error_text2(self):
        errorinfo=self.findElement(self.errorinfo2)
        return self.getText(errorinfo)
    def is_ip_errorinfo_displayed(self):
        errorinfo=self.findElement(self.errorinfo)
        return self.elementdisplay(errorinfo)
    def is_startip_errorinfo_displayed(self):
        errorinfo=self.findElement(self.errorinfo2)
        return self.elementdisplay(errorinfo)
    def wait_alert_invisibale(self):
        self.waituntilinvisible(self.popalert)
    def second_goto_lan(self):
        self.rightpasword = right_password()
        password = self.findElement(self.passwordinputbox)
        self.type(password, self.rightpasword)
        loginbox = self.findElement(self.loginbutton)
        self.click(loginbox)
        time.sleep(5)
        morebox = self.findElement(self.more)
        self.click(morebox)
        time.sleep(3)
        lanset = self.findElement(self.lanset)
        self.click(lanset)
    def click_dhcp_button(self):
        dhcpbutton=self.findElement(self.dhcpbutton)
        self.click(dhcpbutton)
    def is_dhcp_pool_displayed(self):
        dhcppool=self.findElement(self.dhcppool)
        return self.elementdisplay(dhcppool)

    def scroll_window(self):
        js = "window.scrollBy(0,document.body.scrollHeight)"
        self.runJs(js)





