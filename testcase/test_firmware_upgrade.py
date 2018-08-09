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
class FirmwareUpgrade(unittest.TestCase):
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
        self.testcaseinfo = TestCaseInfo(id=40, name="上传错误的升级文件时，错误提示 ")
    def test_FirmwareUpgrade(self):
        try:
            self.starttime = time.strftime("%Y-%m-%d %H:%M:%S")
            self.testcaseinfo.starttime = self.starttime
            self.setuppage.goto_setup()
            time.sleep(5)
            self.setuppage.click_firmware_upgrade()
            time.sleep(3)
            self.setuppage.scroll_window()

            self.setuppage.click_file()
            time.sleep(5)
            cmd = "./upgrade/upload.exe" + " " + uploadpng()
            self.log.info(cmd)

            # 调用autoit脚本选择文件
            self.log.info("开始用autoit3脚本控制选择本地文件")
            ps = subprocess.Popen(cmd)
            ps.wait()
            time.sleep(10)
            self.setuppage.scroll_window()
            self.setuppage.click_begin_upload()
            if self.setuppage.is_uploaderror_displayed():
                errorinfo=self.setuppage.get_uploaderror_text()

                try:
                    self.assertEqual(errorinfo, "文件类型错误，应选择*.bin或*.img。")
                except Exception as e:
                    self.log.error(traceback.format_exc())
                    self.testcaseinfo.result = "Fail"
                    self.testcaseinfo.errorinfo = str(e)
                else:
                    self.testcaseinfo.result = "Pass"
            else:
                self.testcaseinfo.result = "Fail"

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
        try:
            tr.write_data(newreprs, self.teststarttime, int(self.row), *list(self.testcaseinfo.get_case_info()))
        except Exception as err:
            self.log.error(traceback.format_exc())
        finally:
            newrepr.save(self.reportfile)

