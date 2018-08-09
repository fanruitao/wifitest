import unittest
import time
import configparser
from  webpage.SetupPage  import SetupPage
from  common.commonconfig import base_url,uploadpng
from common.logger import logger
from common.testcaseinfo import TestCaseInfo
import xlwt,xlrd
from xlutils.copy import  copy
from common import testreport as tr
import traceback
import subprocess
from datetime import datetime
class CancelReboot(unittest.TestCase):
    def setUp(self):
        self.baseurl = base_url()

        self.setuppage = SetupPage()

        config = configparser.ConfigParser()
        config.read(r"./common/data.ini")
        self.filepath = config.get("logfile", "logfile")
        self.reportfile = config.get("report", "xlsfile")
        self.row = config.get("report", "line")
        self.teststarttime = config.get("teststarttime", "teststarttime")
        config.set("report", "line", str(int(self.row) + 1))
        config.write(open("./common/data.ini", "w"))
        print(self.filepath)
        self.log = logger(self.filepath)
        self.testcaseinfo = TestCaseInfo(id=42, name="取消重启检查 ")
    def test_cancel_reboot(self):
        try:
            self.starttime = time.strftime("%Y-%m-%d %H:%M:%S")
            self.testcaseinfo.starttime = self.starttime
            self.setuppage.goto_setup()
            time.sleep(5)
            self.setuppage.click_reboot_and_recovery()
            time.sleep(2)
            self.setuppage.scroll_window()

            self.setuppage.click_reboot_button()
            time.sleep(3)
            self.setuppage.click_cancel_reboot()
            #再次打开登录页如果还能打开说明重启功能已经被取消
            self.setuppage.open(base_url())
            try:
                self.assertEqual(self.setuppage.getCurrentUrl(), "http://192.168.0.1/Login.html")
            except Exception as e:
                self.log.error(traceback.format_exc())
                self.testcaseinfo.result = "Fail"
                self.testcaseinfo.errorinfo = str(e)
            else:
                self.testcaseinfo.result = "Pass"
        except Exception as err:
            self.testcaseinfo.errorinfo = str(err)
            self.testcaseinfo.result = "error"
            self.log.error(traceback.format_exc())

    def tearDown(self):
        endtime = time.strftime("%Y-%m-%d %H:%M:%S")
        self.testcaseinfo.endtime = endtime

        self.testcaseinfo.secondsDuration = str(datetime.strptime(endtime, "%Y-%m-%d %H:%M:%S") \
                                                - datetime.strptime(self.starttime, "%Y-%m-%d %H:%M:%S"))
        self.log.info([self.testcaseinfo.get_case_info()])
        self.setuppage.quit()
        repr = xlrd.open_workbook(self.reportfile, formatting_info=True)
        self.log.info(repr)
        newrepr = copy(repr)
        self.log.info(newrepr)
        newreprs = newrepr.get_sheet(0)
        tr.write_data(newreprs,self.teststarttime, int(self.row), *list(self.testcaseinfo.get_case_info()))
        newrepr.save(self.reportfile)

