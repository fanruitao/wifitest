#coding=utf-8
import unittest
import time
import configparser
from  webpage.LoginPage  import LoginPage
from  common.commonconfig import base_url
from common.logger import logger
from common.testcaseinfo import TestCaseInfo
import xlwt,xlrd
from xlutils.copy import  copy
from common import testreport as tr
import traceback
from datetime import datetime
from selenium.common.exceptions import WebDriverException
class GotoLogin(unittest.TestCase):
    """登录首页测试用例"""
    def setUp(self):

        self.baseurl=base_url()

        self.loginpage = LoginPage()

        config=configparser.ConfigParser()
        config.read(r"./common/data.ini")
        self.filepath=config.get("logfile","logfile")
        self.reportfile=config.get("report","xlsfile")
        self.teststarttime = config.get("teststarttime", "teststarttime")
        self.row=config.get("report","line")
        config.set("report", "line",str(int(self.row)+1))
        config.write(open("./common/data.ini", "w"))
        print(self.filepath)
        self.log = logger(self.filepath)
        self.testcaseinfo=TestCaseInfo(id=1, name="登录页面跳转测试 ")

    def test_goto_login(self):

        """登录页跳转测试"""
        format = "%a %b %d %H:%M:%S %Y"
        try:
            self.log.info("test_goto_login: test START ")
            # starttime=time.time()
            # self.testcaseinfo.starttime=time.ctime(starttime)
            self.starttime=time.strftime("%Y-%m-%d %H:%M:%S")
            self.testcaseinfo.starttime=self.starttime
            baseurl=self.baseurl
            loginpage=self.loginpage
            loginpage.open(self.baseurl)
            time.sleep(2)
            title=loginpage.getTitle()
            try:
                self.assertEqual('DIR-823Pro',title)
            except Exception as e:
                self.log.error(traceback.format_exc())
                self.testcaseinfo.result = "Fail"
                self.testcaseinfo.errorinfo = str(e)
                # raise AssertionError(traceback.format_exc())
            else:

                self.testcaseinfo.result="Pass"

            # endtime=time.time()
            # self.testcaseinfo.endtime =time.ctime(endtime)
            endtime=time.strftime("%Y-%m-%d %H:%M:%S")
            self.testcaseinfo.endtime=endtime

            self.testcaseinfo.secondsDuration= str(datetime.strptime(endtime,"%Y-%m-%d %H:%M:%S")\
                                                   -datetime.strptime(self.starttime,"%Y-%m-%d %H:%M:%S"))
        except Exception as err:
            self.testcaseinfo.errorinfo = str(err)
            self.testcaseinfo.result="error"
            self.log.error(traceback.format_exc())
    def tearDown(self):
        endtime = time.strftime("%Y-%m-%d %H:%M:%S")
        self.testcaseinfo.endtime = endtime

        self.testcaseinfo.secondsDuration = str(datetime.strptime(endtime, "%Y-%m-%d %H:%M:%S") \
                                                - datetime.strptime(self.starttime, "%Y-%m-%d %H:%M:%S"))
        self.log.info([self.testcaseinfo.get_case_info()])
        self.loginpage.quit()

        repr=xlrd.open_workbook(self.reportfile,formatting_info=True)

        self.log.info(repr)
        newrepr=copy(repr)
        self.log.info(newrepr)
        newreprs=newrepr.get_sheet(0)
        tr.write_data(newreprs,self.teststarttime,int(self.row),*list(self.testcaseinfo.get_case_info()))
        newrepr.save(self.reportfile)











# if __name__ == '__main__':
#     unittest.main()