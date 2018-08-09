import unittest
import time
from  webpage.LoginPage  import LoginPage
from  common.commonconfig import base_url,right_password
from common.logger import logger
from common.testcaseinfo import TestCaseInfo
import configparser
import xlwt,xlrd
from xlutils.copy import  copy
import traceback
from datetime import datetime
from common import testreport as tr


class LoginRight(unittest.TestCase):
    """登录首页测试用例"""
    def setUp(self):

        self.baseurl=base_url()
        self.loginpage = LoginPage()
        self.testcaseinfo=TestCaseInfo(id=2, name="正确密码是否可成功登录测试 ")

        config = configparser.ConfigParser()
        config.read(r"./common/data.ini")
        filepath = config.get("logfile", "logfile")
        self.log = logger(filepath)
        self.reportfile = config.get("report", "xlsfile")
        self.row = config.get("report", "line")
        self.teststarttime = config.get("teststarttime", "teststarttime")
        config.set("report", "line", str(int(self.row) + 1))
        config.write(open("./common/data.ini", "w"))
        #读取报告行数和报告名称


    def test_login_right(self):
        """正确的密码登录是否能登录成功"""
        try:

            # L.info("test_login_right: test START")
            # starttime=time.time()
            # self.testcaseinfo.starttime=time.ctime(starttime)
            self.starttime = time.strftime("%Y-%m-%d %H:%M:%S")
            self.testcaseinfo.starttime = self.starttime

            baseurl=self.baseurl
            loginpage=self.loginpage
            loginpage.open(self.baseurl)
            time.sleep(5)
            password=right_password()
            loginpage.input_password(password)
            time.sleep(2)
            loginpage.click_login()
            time.sleep(5)
            expecturl='http://192.168.0.1/Home.html'
            currenturl=loginpage.getCurrentUrl()
            try:
                self.assertEqual(expecturl,currenturl)
            except Exception as e:
                self.log.error(traceback.format_exc())
                self.testcaseinfo.result = "Fail"
                self.testcaseinfo.errorinfo = str(e)
            else:
                self.testcaseinfo.result = "Pass"

            # endtime = time.time()
            # self.testcaseinfo.endtime = time.ctime(endtime)
            #
            # self.testcaseinfo.secondsDuration= endtime - starttime
            # # L.info([self.testcaseinfo.getcaseinfo()])
            endtime = time.strftime("%Y-%m-%d %H:%M:%S")
            self.testcaseinfo.endtime = endtime

            self.testcaseinfo.secondsDuration = str(datetime.strptime(endtime, "%Y-%m-%d %H:%M:%S") \
                                                    - datetime.strptime(self.starttime, "%Y-%m-%d %H:%M:%S"))
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
        self.loginpage.quit()
        repr = xlrd.open_workbook(self.reportfile, formatting_info=True)
        self.log.info(repr)
        newrepr = copy(repr)
        self.log.info(newrepr)
        newreprs = newrepr.get_sheet(0)
        tr.write_data(newreprs,self.teststarttime, int(self.row), *list(self.testcaseinfo.get_case_info()))
        newrepr.save(self.reportfile)
