import unittest
import time
import configparser
from  webpage.WanPage  import WanPage
from  common.commonconfig import ip_address,mask
from common.logger import logger
from common.testcaseinfo import TestCaseInfo
import xlwt,xlrd
from xlutils.copy import  copy
from common import testreport as tr
import  traceback
from datetime import datetime
class NoMask(unittest.TestCase):
    def setUp(self):

        self.testcaseinfo = TestCaseInfo(id=8, name="不输入默认网关时的错误信息提示 ")

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
        self.webpage=WanPage()

    def test_no_mask(self):
        """不输入子网掩码时的错误信息提示"""
        try:

            self.starttime = time.strftime("%Y-%m-%d %H:%M:%S")
            self.testcaseinfo.starttime = self.starttime
            self.webpage.goto_wan()
            time.sleep(5)
            self.webpage.chose_staticip()
            time.sleep(2)
            self.webpage.set_ip_address(ip_address())
            self.webpage.set_mask(mask())
            self.webpage.scroll_window()
            self.webpage.click_save()
            time.sleep(5)
            if self.webpage.is_gatewayerr_display():
                errorinfo=self.webpage.get_error_text2()
                self.log.info(errorinfo)
                try:
                    self.assertEqual(errorinfo,"请输入默认网关地址。")
                except Exception as e:
                    self.log.error(traceback.format_exc())
                    self.testcaseinfo.result = "Fail"
                    self.testcaseinfo.errorinfo = str(e)
                else:
                    self.testcaseinfo.result = "Pass"
            else:
                self.testcaseinfo.result = "error"

            endtime = time.strftime("%Y-%m-%d %H:%M:%S")
            self.testcaseinfo.endtime = endtime

            self.testcaseinfo.secondsDuration = str(datetime.strptime(endtime, "%Y-%m-%d %H:%M:%S") \
                                                    - datetime.strptime(self.starttime, "%Y-%m-%d %H:%M:%S"))

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
        self.webpage.quit()
        repr = xlrd.open_workbook(self.reportfile, formatting_info=True)
        self.log.info(repr)
        newrepr = copy(repr)
        self.log.info(newrepr)
        newreprs = newrepr.get_sheet(0)
        tr.write_data(newreprs,self.teststarttime, int(self.row), *list(self.testcaseinfo.get_case_info()))
        newrepr.save(self.reportfile)

if __name__ == '__main__':
    unittest.main()