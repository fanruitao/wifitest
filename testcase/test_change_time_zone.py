import unittest
import time
import configparser
from  webpage.SetupPage  import SetupPage
from  common.commonconfig import base_url
from common.logger import logger
from common.testcaseinfo import TestCaseInfo
import xlwt,xlrd
from xlutils.copy import  copy
from common import testreport as tr
import traceback
from datetime import datetime
class ChangeTimeZone(unittest.TestCase):
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
        self.testcaseinfo = TestCaseInfo(id=39, name="检查时区能否正确改变 ")
    def test_change_time_zone(self):
        try:
            self.starttime = time.strftime("%Y-%m-%d %H:%M:%S")
            self.testcaseinfo.starttime = self.starttime
            self.setuppage.goto_setup()
            time.sleep(5)
            self.setuppage.click_internet_time()
            time.sleep(3)
            self.setuppage.chose_7_zone()
            time.sleep(2)
            self.setuppage.scroll_window()
            self.setuppage.click_savebutton()
            self.setuppage.wait_alert_invisiable()
            time.sleep(5)
            selecttext=self.setuppage.get_select_text()
            try:
                self.assertEqual(selecttext, "CST+7 (MST-北美山区标准时间)")
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
        self.log.info("测试完成恢复时区")
        self.setuppage.chose_8_zone()
        time.sleep(2)
        self.setuppage.click_savebutton()
        self.setuppage.wait_alert_invisiable()
        self.setuppage.quit()
        repr = xlrd.open_workbook(self.reportfile, formatting_info=True)
        self.log.info(repr)
        newrepr = copy(repr)
        self.log.info(newrepr)
        newreprs = newrepr.get_sheet(0)
        try:
            tr.write_data(newreprs, self.teststarttime, int(self.row), *list(self.testcaseinfo.get_case_info()))
        except Exception as err:
            self.log.error(traceback.format_exc())
        finally:
            newrepr.save(self.reportfile)

