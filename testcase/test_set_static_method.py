import unittest
import time
import configparser
from  webpage.WanPage  import WanPage
from  common.commonconfig import ip_address,mask,gateway,dns
from common.logger import logger
from common.testcaseinfo import TestCaseInfo
import xlwt,xlrd
from xlutils.copy import  copy
from common import testreport as tr
import  traceback
from datetime import datetime

class SetStaticMethod(unittest.TestCase):
    def setUp(self):

        self.testcaseinfo = TestCaseInfo(id=12, name="是否可以成功设置静态IP ")

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

    def test_set_static_method(self):

        try:

            self.starttime = time.strftime("%Y-%m-%d %H:%M:%S")
            self.testcaseinfo.starttime = self.starttime
            self.webpage.goto_wan()
            time.sleep(5)
            self.webpage.chose_staticip()
            time.sleep(2)
            self.webpage.set_ip_address(ip_address())
            self.webpage.set_mask(mask())
            self.webpage.set_gateway(gateway())
            self.webpage.set_dns(dns())
            self.webpage.scroll_window()
            time.sleep(2)
            self.webpage.click_save()
            time.sleep(15)
            try:
                self.assertEqual("手动输入IP(静态IP)",self.webpage.get_internettype())
            except Exception as e:
                self.log.error(traceback.format_exc())
                self.testcaseinfo.errorinfo = str(e)
                self.testcaseinfo.result="Fail"
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
        self.log.info("测试完成后将上网方式恢复为自动获取")
        try:
            self.webpage.chose_DHCP()
            self.webpage.scroll_window()
            self.webpage.click_save()
            time.sleep(15)
        except Exception as err:
            self.log.error(traceback.format_exc())
        finally:
            self.webpage.quit()
            repr = xlrd.open_workbook(self.reportfile, formatting_info=True)
            self.log.info(repr)
            newrepr = copy(repr)
            self.log.info(newrepr)
            newreprs = newrepr.get_sheet(0)
            tr.write_data(newreprs, self.teststarttime,int(self.row), *list(self.testcaseinfo.get_case_info()))
            newrepr.save(self.reportfile)

if __name__ == '__main__':
    unittest.main()