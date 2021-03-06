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
import subprocess
import re
from datetime import datetime
class SsidClose(unittest.TestCase):
    def setUp(self):

        self.testcaseinfo = TestCaseInfo(id=31, name="关闭SSID,查看电脑列表能否搜索到wifi名称 ")

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

    def test_ssid_close(self):
        """正确的密码登录是否能登录成功"""
        try:

            self.starttime = time.strftime("%Y-%m-%d %H:%M:%S")
            self.testcaseinfo.starttime =self.starttime
            self.wifipage.goto_gaoji_page()
            time.sleep(5)
            self.wifipage.scroll_window2()
            time.sleep(6)
            self.wifipage.click_ssid_hide()
            self.wifipage.scroll_window()
            self.wifipage.click_ssid_save()
            time.sleep(20)
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
        self.log.info("测试完成后关闭ssid隐藏")
        try:
            self.wifipage.click_ssid_hide()
            self.wifipage.scroll_window()
            self.wifipage.click_ssid_save()
            time.sleep(20)
        except Exception as err:
            self.log.error(traceback.format_exc())
        finally:
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