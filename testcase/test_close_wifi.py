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
import subprocess,re
from datetime import datetime
class CloseWifi(unittest.TestCase):
    def setUp(self):

        self.testcaseinfo = TestCaseInfo(id=30, name="关闭wifi 后，查看电脑的无线列表 ")

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

    def test_close_wifi(self):
        """正确的密码登录是否能登录成功"""
        try:

            # L.info("test_login_right: test START")
            self.starttime = time.strftime("%Y-%m-%d %H:%M:%S")
            self.testcaseinfo.starttime = self.starttime
            self.wifipage.goto_wifi()
            time.sleep(5)
            self.wifipage.click_wifi_button()
            time.sleep(5)
            self.wifipage.click_wifi_close_confirm()
            self.wifipage.wait_pop_alert_disappear()
            result = True
            p = subprocess.Popen('netsh wlan show network', stdout=subprocess.PIPE)
            # print(p.stdout.readlines())
            for line in p.stdout.readlines():
                if not re.search('SSID\s+\d+\s+:\frt_test', str(line)):
                    self.log.info("no found")
                else:
                    result = False
                    break
            try:
                self.assertTrue(result)
            except Exception as err:
                self.testcaseinfo.errorinfo = str(err)
                self.log.error(traceback.format_exc())
                self.testcaseinfo.result = "Fail"
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
        self.log.info("测试完成后恢复到wifi打开的状态")
        self.wifipage.click_wifi_button()
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