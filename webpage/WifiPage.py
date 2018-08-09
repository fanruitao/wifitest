from webpage.BasePage import BasePage
import time
from  common.commonconfig import base_url,right_password

class WifiPage(BasePage):
    passwordinputbox = ('id', 'admin_Password1')
    loginbutton = ('id', 'logIn_btn')
    wirelessset=('id','wirless')
    wifiname=('id','wifiName_24')
    wifipassword=('id','password1_24')
    savebutton=('xpath','//input[@id="savebutton"]')
    alert=('id','CreatePopAlertMessage')
    confirm=('id','saveconfirm2_5G')
    errorinfo1=('id','errorinfo_1')
    errorinfo2=('id','errorinfo_2')
    wifibutton=('id','wlan_status')
    wificloseconfirm=('id','clowifyconfirm2g')

    morebutton=('xpath','//div[@id="want_more_id"]/div')
    wireless=('id','lang_wirelessSetUp')
    gaoji=('id','lang_advwlanset')
    status=('id','wlan_status')
    save=('id','savebutton')

    def __init__(self,browser = 'chrome'):
        super().__init__(browser)
        print(self.driver)
    def goto_wifi(self):
        self.baseurl = base_url()
        self.rightpasword = right_password()
        self.open(self.baseurl)
        time.sleep(5)
        password = self.findElement(self.passwordinputbox)
        self.type(password, self.rightpasword)
        loginbox = self.findElement(self.loginbutton)
        self.click(loginbox)
        time.sleep(5)
        wireless=self.findElement(self.wirelessset)
        self.click(wireless)
    def get_wifi_name(self):
        wifiname=self.findElement(self.wifiname)
        return self.getAttribute(wifiname,'value')
    def get_wifi_password(self):
        wifipassword=self.findElement(self.wifipassword)
        return self.getAttribute(wifipassword,'value')
    def set_wifi_name(self,value):
        wifiname = self.findElement(self.wifiname)
        self.type(wifiname,value)
    def set_wifi_password(self,value):
        wifipassword = self.findElement(self.wifipassword)
        self.type(wifipassword,value)
    def clear_wifi_name(self):
        wifiname = self.findElement(self.wifiname)
        self.clear(wifiname)
    def clear_wifi_password(self):
        wifipassword = self.findElement(self.wifipassword)
        self.clear(wifipassword)
    def click_savebutton(self):
        savebutton=self.findElement(self.savebutton)
        self.click(savebutton)
    def wait_pop_alert_disappear(self):
        self.waituntilinvisible(self.alert)
    def click_confirm(self):
        confirm=self.findElement(self.confirm)
        self.click(confirm)
    def click_wifi_button(self):
        wifibutton=self.findElement(self.wifibutton)
        self.click(wifibutton)
    def click_wifi_close_confirm(self):
        wificloseconfirm=self.findElement(self.wificloseconfirm)
        self.click(wificloseconfirm)
    def scroll_window(self):
        js="window.scrollBy(0,document.body.scrollHeight)"
        self.runJs(js)
    def scroll_window2(self):
        #将滚动条滑动到固定位置
        js="window.scrollBy(0,700)"
        self.runJs(js)

    def is_error_info1_displayed(self):
        errorinfo1=self.findElement(self.errorinfo1)
        return self.elementdisplay(errorinfo1)
    def is_error_info2_displayed(self):
        errorinfo2=self.findElement(self.errorinfo2)
        return self.elementdisplay(errorinfo2)
    def get_error_info1(self):
        errorinfo1 = self.findElement(self.errorinfo1)
        return self.getText(errorinfo1)
    def get_error_info2(self):
        errorinfo2 = self.findElement(self.errorinfo2)
        return self.getText(errorinfo2)
    def goto_gaoji_page(self):
        self.baseurl = base_url()
        self.rightpasword = right_password()
        self.open(self.baseurl)
        time.sleep(5)
        password = self.findElement(self.passwordinputbox)
        self.type(password, self.rightpasword)
        loginbox = self.findElement(self.loginbutton)
        self.click(loginbox)
        time.sleep(5)

        more=self.findElement(self.morebutton)
        self.click(more)
        time.sleep(2)
        wireless=self.findElement(self.wireless)
        self.click(wireless)
        time.sleep(2)
        gaoji=self.findElement(self.gaoji)
        self.click(gaoji)
        time.sleep(5)
    def click_ssid_hide(self):
        ssidstatus=self.findElement(self.status)
        self.click(ssidstatus)
    def click_ssid_save(self):
        save=self.findElement(self.save)
        self.click(save)





