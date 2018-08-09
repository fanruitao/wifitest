from webpage.BasePage import BasePage
import time
from  common.commonconfig import base_url,right_password

class WanPage(BasePage):
    """上网设置页面"""
    passwordinputbox = ('id', 'admin_Password1')
    loginbutton = ('id', 'logIn_btn')
    internetset = ('xpath', "//div[@id='want_internet_id']/div/span")
    selectbox=('id','select_networktype')
    ipbox=("id","staticIpaddr")
    savebox=("id","savebutton")
    iperror=("id","errorinfo_4")
    maskbox=("id","staticmask")
    gatewaybox=("id","staticgateway")
    maskerror=("id","errorinfo_5")
    gatewayerror=("id","errorinfo_6")
    internettype=("id","networktypeinfo")
    dnsbox=("id","staticdns1")

    def __init__(self,browser = 'chrome'):
        super().__init__(browser)
        print(self.driver)

    def goto_wan(self):
        self.baseurl = base_url()
        self.rightpasword = right_password()
        self.open(self.baseurl)
        time.sleep(5)
        password=self.findElement(self.passwordinputbox)
        self.type(password,self.rightpasword)
        loginbox=self.findElement(self.loginbutton)
        self.click(loginbox)
        time.sleep(5)
        internetsetbox = self.findElement(self.internetset)
        self.click(internetsetbox)
    def chose_staticip(self):
        js='document.querySelectorAll("select")[0].style.display="block";'
        self.runJs(js)
        time.sleep(5)
        self.selectbyvalue(self.selectbox,'Static')
    def chose_DHCP(self):
        js = 'document.querySelectorAll("select")[0].style.display="block";'
        self.runJs(js)
        time.sleep(5)
        self.selectbyvalue(self.selectbox,'DHCP')
    def click_save(self):
        savebutton=self.findElement(self.savebox)
        self.click(savebutton)
    def is_iperr_display(self):
        iperror=self.findElement(self.iperror)
        return self.elementdisplay(iperror)
    def is_maskerr_display(self):
        maskerror = self.findElement(self.maskerror)
        return self.elementdisplay(maskerror)
    def is_gatewayerr_display(self):
        gatewayerror = self.findElement(self.gatewayerror)
        return self.elementdisplay(gatewayerror)

    def get_error_text(self):
        iperror=self.findElement(self.iperror)
        return self.getText(iperror)

    def get_error_text1(self):
        maskerror = self.findElement(self.maskerror)
        return self.getText(maskerror)

    def get_error_text2(self):
        gatewayerror = self.findElement(self.gatewayerror)
        return self.getText(gatewayerror)
    def set_ip_address(self,text):
        ipaddressinput=self.findElement(self.ipbox)
        return self.type(ipaddressinput,text)
    def set_mask(self,text):
        maskinput = self.findElement(self.maskbox)
        return self.type(maskinput, text)
    def set_gateway(self,text):
        gatewayinput=self.findElement(self.gatewaybox)
        return self.type(gatewayinput,text)
    def set_dns(self,text):
        dnsinput=self.findElement(self.dnsbox)
        return self.type(dnsinput,text)

    def clear_ip(self):
        ipaddressinput = self.findElement(self.ipbox)
        ipaddressinput.clear()
    def clear_mask(self):
        maskinput = self.findElement(self.maskbox)
        maskinput.clear()
    def clear_gateway(self):
        gatewayinput = self.findElement(self.gatewaybox)
        gatewayinput.clear()
    def get_internettype(self):
        internettype=self.findElement(self.internettype)
        return self.getText(internettype)

    def scroll_window(self):
        js = "window.scrollBy(0,document.body.scrollHeight)"
        self.runJs(js)














