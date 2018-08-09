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
class NoWifiPasswordEnter(unittest.TestCase):
    def setUp(self):
        #默认项检查，目前假设默认wifi 名字是frt_test,密码时iot23321
        self.testcaseinfo = TestCaseInfo(id=27, name="不输入wifi密码时是否可以保存成功 ")

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

    def test_no_wifi_password_enter(self):
        """不填写密码时，可以保存成功，自动化脚本无法检测是否不填写无线密码就可以不输入密码直接连上"""
        try:

            # L.info("test_login_right: test START")
            self.starttime = time.strftime("%Y-%m-%d %H:%M:%S")
            self.testcaseinfo.starttime = self.starttime
            self.wifipage.goto_wifi()
            time.sleep(5)
            self.wifipage.clear_wifi_password()
            self.wifipage.scroll_window()
            self.wifipage.click_savebutton()
            time.sleep(3)
            self.wifipage.click_confirm()
            self.wifipage.wait_pop_alert_disappear()
            time.sleep(5)
            password=self.wifipage.get_wifi_password()
            try:
                self.assertEqual(password, "")
            except Exception as e:
                self.log.error(traceback.format_exc())
                self.testcaseinfo.result = "Fail"
                self.testcaseinfo.errorinfo = str(e)
            else:
                self.testcaseinfo.result = "Pass"

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
        self.log.info("测试完成后恢复wifi密码")

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