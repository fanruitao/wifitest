import unittest
import time
import configparser
from  webpage.WifiPage import  WifiPage
from  common.commonconfig import base_url
from common.logger import logger
from common.testcaseinfo import TestCaseInfo
import xlwt,xlrd
from xlutils.copy import  copy
from common import testreport as tr
import  traceback
from datetime import datetime

class LegalWifiPassword(unittest.TestCase):
    def setUp(self):
        #默认项检查，目前假设默认wifi 名字是frt_test,密码时iot23321
        self.testcaseinfo = TestCaseInfo(id=29, name="是否支持各种格式的wifi密码 ")

        config = configparser.ConfigParser()
        config.read(r"./common/data.ini")
        filepath = config.get("logfile", "logfile")
        self.log = logger(filepath)
        self.reportfile = config.get("report", "xlsfile")
        self.row = config.get("report", "line")
        self.teststarttime = config.get("teststarttime", "teststarttime")
        config.set("report", "line", str(int(self.row) + 1))
        config.write(open("./common/data.ini", "w"))
        # 读取报告行数和报告名称
        self.wifipage=WifiPage()

    def test_legal_wifi_password(self):
        """正确的密码登录是否能登录成功"""
        try:

            self.starttime = time.strftime("%Y-%m-%d %H:%M:%S")
            self.testcaseinfo.starttime = self.starttime
            self.wifipage.goto_wifi()
            time.sleep(5)
            result=0
            wifipassword = ["werwerwer", ":#$@Q#$@Q#$@Q", "@!$as@!$as@!$as", "@#$12@#$12", "!@#$%^a!", "iot123321"]
            for i in wifipassword:
                time.sleep(2)
                self.wifipage.clear_wifi_password()
                self.wifipage.set_wifi_password(i)
                self.wifipage.scroll_window()
                self.wifipage.click_savebutton()
                time.sleep(5)
                self.wifipage.click_confirm()
                self.wifipage.wait_pop_alert_disappear()
                time.sleep(5)
                if self.wifipage.get_wifi_password()==i:
                    result+=1
                else:
                    self.testcaseinfo.result="Fail"
            try:
                self.assertEqual(result,len(wifipassword))
            except Exception as err:
                self.testcaseinfo.errorinfo = str(err)
                self.log.error(traceback.format_exc())
                self.testcaseinfo.result = "Fail"
            else:
                self.testcaseinfo.result="Pass"

        except Exception as err:
            self.testcaseinfo.errorinfo = str(err)
            self.log.error(traceback.format_exc())
            self.testcaseinfo.result = "error"

    def tearDown(self):
        endtime = time.strftime("%Y-%m-%d %H:%M:%S")
        self.testcaseinfo.endtime = endtime

        self.testcaseinfo.secondsDuration = str(datetime.strptime(endtime, "%Y-%m-%d %H:%M:%S") \
                                                - datetime.strptime(self.starttime, "%Y-%m-%d %H:%M:%S"))
        self.log.info([self.testcaseinfo.get_case_info()])
        self.log.info("测试完成恢复wifi密码")
        time.sleep(3)
        self.wifipage.clear_wifi_password()
        time.sleep(3)
        self.wifipage.set_wifi_password("iot123321")
        self.wifipage.scroll_window()
        self.wifipage.click_savebutton()
        time.sleep(5)
        self.wifipage.click_confirm()
        self.wifipage.wait_pop_alert_disappear()
        self.wifipage.quit()
        repr = xlrd.open_workbook(self.reportfile, formatting_info=True)
        self.log.info(repr)
        newrepr = copy(repr)
        self.log.info(newrepr)
        newreprs = newrepr.get_sheet(0)
        tr.write_data(newreprs,self.teststarttime, int(self.row), *list(self.testcaseinfo.get_case_info()))
        newrepr.save(self.reportfile)

# if __name__ == '__main__':
#     unittest.main()