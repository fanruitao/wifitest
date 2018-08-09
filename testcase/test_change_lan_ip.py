import unittest
import time
import  re
import configparser
from  webpage.LanPage  import LanPage
from  common.commonconfig import base_url,new_lan_ip
from common.logger import logger
from common.testcaseinfo import TestCaseInfo
import xlwt,xlrd
from xlutils.copy import  copy
from common import testreport as tr
import  traceback
from datetime import datetime
class ChangeLanIp(unittest.TestCase):
    def setUp(self):

        self.testcaseinfo = TestCaseInfo(id=17, name="lan页面修改局域网地址是否可以成功 ")

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

    def test_change_lan_ip(self):
        """正确的密码登录是否能登录成功"""
        try:

            # L.info("test_login_right: test START")
            self.starttime = time.strftime("%Y-%m-%d %H:%M:%S")
            self.testcaseinfo.starttime = self.starttime
            self.lanpage.goto_lan()
            time.sleep(5)
            self.lanpage.clear_lanip()
            time.sleep(2)
            self.lanpage.set_lanip(new_lan_ip())
            self.lanpage.scroll_window()

            self.lanpage.click_savebutton()
            self.lanpage.wait_alert_invisibale()

            time.sleep(5)
            try:
                self.assertEqual(self.lanpage.getCurrentUrl(),"http://" + str(new_lan_ip()) + "/Login.html")
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
        self.log.info("测试完成后修改到原来的IP")
        self.lanpage.second_goto_lan()
        time.sleep(3)
        self.lanpage.clear_lanip()
        self.lanpage.set_lanip(re.split("//",base_url())[1])
        self.lanpage.scroll_window()
        self.lanpage.click_savebutton()
        self.lanpage.wait_alert_invisibale()


        self.lanpage.quit()
        repr = xlrd.open_workbook(self.reportfile, formatting_info=True)
        self.log.info(repr)
        newrepr = copy(repr)
        self.log.info(newrepr)
        newreprs = newrepr.get_sheet(0)
        tr.write_data(newreprs,self.teststarttime, int(self.row), *list(self.testcaseinfo.get_case_info()))
        newrepr.save(self.reportfile)

