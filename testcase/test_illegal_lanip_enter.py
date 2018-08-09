import unittest
import time
import configparser
from  webpage.LanPage  import LanPage
from common.logger import logger
from common.testcaseinfo import TestCaseInfo
import xlwt,xlrd
from xlutils.copy import  copy
from common import testreport as tr
import  traceback
from datetime import datetime
class IllegalLanipEnter(unittest.TestCase):
    def setUp(self):

        self.testcaseinfo = TestCaseInfo(id=16, name="lan页面输入格式错误的局域网地址时的提示语检查 ")

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
        self.lanpage=LanPage()

    def test_illegal_lanip_enter(self):
        """正确的密码登录是否能登录成功"""
        try:

            # L.info("test_login_right: test START")
            self.starttime = time.strftime("%Y-%m-%d %H:%M:%S")
            self.testcaseinfo.starttime = self.starttime
            self.lanpage.goto_lan()
            time.sleep(5)
            self.lanpage.clear_lanip()
            result=0
            wrongip = ['192.168.www.4', '192.!23.tt.com', '192.168.%$.#', '1 92.168.  34', '192.168.344.2',
                       '192.-168.3.2']
            for ip in wrongip:
                self.lanpage.clear_lanip()
                self.lanpage.set_lanip(ip)
                self.lanpage.scroll_window()
                time.sleep(2)
                self.lanpage.click_savebutton()
                if self.lanpage.is_ip_errorinfo_displayed():
                    errorinfo = self.lanpage.get_error_text()
                    self.log.info(errorinfo)
                    if errorinfo=="IP地址含非法字符，请重新输入。" or errorinfo=="IP地址格式错误，请重新输入。":
                        result+=1
                    else:
                        self.testcaseinfo.result='Fail'
            try:
                self.assertEqual(len(wrongip),result)
                self.testcaseinfo.result = "Pass"
            except Exception as e:
                self.log.error(traceback.format_exc())
                self.testcaseinfo.result = "Fail"
                self.testcaseinfo.errorinfo = str(e)
                self.testcaseinfo.result = "Fail"
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
        self.lanpage.quit()
        repr = xlrd.open_workbook(self.reportfile, formatting_info=True)
        self.log.info(repr)
        newrepr = copy(repr)
        self.log.info(newrepr)
        newreprs = newrepr.get_sheet(0)
        tr.write_data(newreprs,self.teststarttime, int(self.row), *list(self.testcaseinfo.get_case_info()))
        newrepr.save(self.reportfile)

