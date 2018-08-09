from webpage.BasePage import BasePage
import time
from  common.commonconfig import base_url,right_password,original_login_password,new_login_password

class SetupPage(BasePage):
    passwordinputbox = ('id', 'admin_Password1')
    loginbutton = ('id', 'logIn_btn')
    morebutton = ('xpath', '//div[@id="want_more_id"]/div')
    systemmanage=('id','ic_systemSetup')
    modifypassword=('xpath','//li[@id="liaccount"]/a')
    savebutton=('id','savebutton5')
    errorinfo1=('id','errorinfo_1')
    errorinfo2 = ('id', 'errorinfo_2')
    errorinfo3 = ('id', 'errorinfo_3')
    originalpassword=('id','current_password')
    newpassword=('id','new_password')
    confirmpassword=('id','confirm_password')
    internertime=('id','lang_time')
    selectbox=('id','select_zone')
    alert=('id','CreateOnloadMessage')
    selecttext=('class','sbSelector')
    firmwareup=('id','lang_upgrade')
    chosefirmware=('css','label.styled_button_s')
    beginuploadbutton=('id','btn_begin_upload')
    uploaderror=('id','errorinfo_update')
    rebootandrecover=('id','lang_reboot')
    rebootbutton=('id','btn_reboot_router')
    rebootconfirm=('id','btn_reboot_confirm')
    rebootingalert=('id','DeviceRebooting')
    cancelrebootbutton=('id','btn_reboot_cancel')

    def __init__(self, browser='chrome'):
        super().__init__(browser)
        print(self.driver)
    def goto_setup(self):
        self.baseurl = base_url()
        self.rightpasword = right_password()
        self.open(self.baseurl)
        time.sleep(5)
        password = self.findElement(self.passwordinputbox)
        self.type(password, self.rightpasword)
        loginbox = self.findElement(self.loginbutton)
        self.click(loginbox)
        time.sleep(5)

        more = self.findElement(self.morebutton)
        self.click(more)
        time.sleep(2)
        self.scroll_window()
        time.sleep(3)
        systemmanage=self.findElement(self.systemmanage)
        self.click(systemmanage)

    def goto_setup_use_new_password(self):

        time.sleep(5)
        password = self.findElement(self.passwordinputbox)
        self.type(password, new_login_password())
        loginbox = self.findElement(self.loginbutton)
        self.click(loginbox)
        time.sleep(5)

        more = self.findElement(self.morebutton)
        self.click(more)
        time.sleep(2)
        self.scroll_window()
        systemmanage = self.findElement(self.systemmanage)
        self.click(systemmanage)
    def click_modify_password(self):
        modifypassword=self.findElement(self.modifypassword)
        self.click(modifypassword)
    def click_savebutton(self):
        savebutton=self.findElement(self.savebutton)
        self.click(savebutton)
    def is_error_info1_displayed(self):
        errorinfo1=self.findElement(self.errorinfo1)
        return self.elementdisplay(errorinfo1)

    def is_error_info2_displayed(self):
        errorinfo2 = self.findElement(self.errorinfo2)
        return self.elementdisplay(errorinfo2)

    def is_error_info3_displayed(self):
        errorinfo3 = self.findElement(self.errorinfo3)
        return self.elementdisplay(errorinfo3)

    def get_error_info1_text(self):
        errorinfo1 = self.findElement(self.errorinfo1)
        return self.getText(errorinfo1)

    def scroll_window(self):
        js = "window.scrollBy(0,document.body.scrollHeight)"
        self.runJs(js)
    def scroll_window_to_top(self):
        js="document.getElementsByTagName('body')[0].scrollTop = 0;"
        self.runJs(js)
    def set_original_password(self,text):
        originalpassword=self.findElement(self.originalpassword)
        self.type(originalpassword,text)
    def set_new_password(self,text):
        newpassword=self.findElement(self.newpassword)
        self.type(newpassword,text)

    def set_confirm_password(self, text):
        confirmpassword = self.findElement(self.confirmpassword)
        self.type(confirmpassword, text)
    def get_error_info2_text(self):
        errorinfo2 = self.findElement(self.errorinfo2)
        return self.getText(errorinfo2)
    def get_error_info3_text(self):
        errorinfo3 = self.findElement(self.errorinfo3)
        return self.getText(errorinfo3)


    def click_internet_time(self):
        internettime=self.findElement(self.internertime)
        self.click(internettime)
    def chose_7_zone(self):
        js = 'document.querySelectorAll("select")[0].style.display="block";'
        self.runJs(js)
        self.selectbyvalue(self.selectbox,"CST+7")
    def chose_8_zone(self):
        js = 'document.querySelectorAll("select")[0].style.display="block";'
        self.runJs(js)
        self.selectbyvalue(self.selectbox, "CST-8")
    def wait_alert_invisiable(self):
        self.waituntilinvisible(self.alert)
    def get_select_text(self):
        selecttext=self.findElement(self.selecttext)
        return self.getText(selecttext)


    def click_firmware_upgrade(self):
        firmwareup=self.findElement(self.firmwareup)
        self.click(firmwareup)
    def click_file(self):
        chosefirmware=self.findElement(self.chosefirmware)
        self.click(chosefirmware)
    def click_begin_upload(self):
        beginupload=self.findElement(self.beginuploadbutton)
        self.click(beginupload)
    def is_uploaderror_displayed(self):
        uploaderrror=self.findElement(self.uploaderror)
        return self.elementdisplay(uploaderrror)
    def get_uploaderror_text(self):
        uploaderrror = self.findElement(self.uploaderror)
        return self.getText(uploaderrror)
    def click_reboot_and_recovery(self):
        rebootandrecovery=self.findElement(self.rebootandrecover)
        self.click(rebootandrecovery)
    def click_reboot_button(self):
        rebootbutton=self.findElement(self.rebootbutton)
        self.click(rebootbutton)
    def click_reboot_confirm(self):
        rebootconfirm=self.findElement(self.rebootconfirm)
        self.click(rebootconfirm)
    def wait_rebooting_alert_invisible(self):

        self.waituntilinvisible2(self.rebootingalert)
    def click_cancel_reboot(self):
        cancelreboot=self.findElement(self.cancelrebootbutton)
        self.click(cancelreboot)
















