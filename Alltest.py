
import subprocess
from datetime import datetime
from common.logger import logger
from common import testreport as TT
from common.commonconfig import ifsendmail
from common import sendmail
import  time
import configparser




class RunTests(object):
    """description of class"""

    def __init__(self):

        self.testcaselistfile = "./common/testcases.txt"
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        logpath = './log/' + now + '.log'
        config=configparser.ConfigParser()
        config.read(r"./common/data.ini")
        config.set("logfile","logfile",logpath)
        config.write(open("./common/data.ini", "w"))
        self.log=logger(logpath)

        path = r"./report/%s" % now
        self.xls_file = r"%s.xls" % (path)
        teststarttime=TT.write_title(self.xls_file)
        config.set('teststarttime','teststarttime',teststarttime)
        config.set("report","xlsfile",self.xls_file)
        config.write(open("./common/data.ini", "w"))
    def LoadAndRunTestCases(self):
        try:
            f = open(self.testcaselistfile)
            testfiles = [test for test in f.readlines() if not test.startswith("#")]
            f.close()

            for item in testfiles:
                print("############")
                print(item)
                print("nosetests testcase\\" + str(item).replace("\\n", ""))

                subprocess.call("nosetests testcase\\"+str(item), shell = True)

        except Exception as err:
            self.log.debug("Failed running test cases, error message: {}".format(str(err)))

        if (ifsendmail() == 'True'):
            self.log.info("发送邮件")
            sendmail.send_mail(self.xls_file)
        else:
            self.log.info("测试结束")



if __name__ == "__main__":
    newrun = RunTests()
    newrun.LoadAndRunTestCases()
    #测试完成后，将报告行数的初始值改到12
    config = configparser.ConfigParser()
    config.read(r"./common/data.ini")
    row = config.get("report", "line")
    config.set("report", "line", str(12))
    config.write(open("./common/data.ini", "w"))






