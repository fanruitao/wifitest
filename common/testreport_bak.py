from xml.etree import ElementTree as ET
import datetime
import os
import time

from xlwt import *


'''
# font.bold = True
# font.underline = True
# font.italic = True
XFStyle用于设置字体样式，有描述字符串num_format_str，字体font，
居中alignment，边界borders，模式pattern，保护protection等属性。
另外还可以不写单元格，直接设置格式

  # Create Alignment
#设置单元格对齐方式 
alignment.horz = Alignment.HORZ_CENTER
***May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER,
***HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED,
***HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.vert = Alignment.VERT_CENTER  # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
style = XFStyle()  # Create Style
style.alignment = alignment

# font_sty = [u"微软雅黑", 11]
'''


class WriteXls(object):
    def __init__(self):
        self.run()


    def easy_xf(self):
        self.easyxf1 = easyxf(
            u'font: height 320, name 宋体, colour_index 70, bold on; align: wrap on, vert top, horiz left; borders: top thin, left thin, right thin;')

        self.easyxf2 = easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz left; borders: right thin;')

        self.easyxf3 = easyxf(
            u'font: height 220, name 宋体; align: wrap on; borders: left thin, right thin;')

        self.easyxf4 = easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz left; borders: top thin, bottom thin, left thin, right thin; pattern: pattern solid, fore_colour 22')

        self.easyxf5 = easyxf(
            u'font: height 220, name 宋体, colour_index white, bold on; align: wrap on, horiz left; borders: left thin, right thin; pattern: pattern solid, fore_colour 23')

        self.easyxf6 = easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz centre; borders: top thin, bottom thin, left thin, right thin; pattern: pattern solid, fore_colour 22')

        self.easyxf7 = easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz left; borders: left thin, right thin;')

        self.easyxf8 = easyxf(
            u'font: height 220, name 宋体; align: wrap on; borders: top thin, bottom thin, left thin, right thin;')

        self.easyxf9 = easyxf(
            u'font: height 220, name 宋体, bold on; align: wrap on, horiz left; borders: left thin;')

        self.easyxf10 = easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz right; borders: top thin, bottom thin, left thin, right thin; pattern: pattern solid, fore_colour 22')

        self.easyxf11 = easyxf(
            u'font: height 220, name 宋体, bold on; align: wrap on, horiz left; borders: top thin, bottom thin, left thin;')

        self.easyxf12 = easyxf(
            u'font: height 220, name 宋体, bold on; align: wrap on, horiz left; borders: top thin, bottom thin, right thin;')

        self.easyxf13 = easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz centre; borders: top thin, bottom thin, left thin, right thin;',
            num_format_str="0%")

    def check_path(self):
        current_time = time.strftime("%Y-%m-%d_%H.%M")
        path = r"./report/%s" % current_time
        # if os.path.exists(parent_path) is False:
        #     try:
        #         os.makedirs(parent_path)
        #     except OSError:
        #         import traceback
        #         print (traceback.format_exc())
        self.xls_file = r"%s.xls" % (path)
    def run(self):
        self.easy_xf()
        self.check_path()

        self.case_count = []
        self.total_row = []
        self.book = Workbook(encoding='utf-8')
        self.sheet = self.book.add_sheet("testreport", cell_overwrite_ok=True)
        self.write_title()
        self.book.save(self.xls_file)
        # return self.book,self.sheet

    def write_title(self):
        self.sheet.col(0).width = 256 * 15
        self.sheet.col(1).width = 256 * 50
        for i in range(2, 6):
            self.sheet.col(i).width = 256 * 30
        self.sheet.col(6).width = 256 * 25

        self.sheet.write_merge(0, 1, 0, 6, "测试报告", self.easyxf1)
        self.sheet.write_merge(2, 2, 0, 6, "", self.easyxf3)

        self.start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.sheet.write(3, 0, "开始时间：", self.easyxf9)
        self.sheet.write_merge(3, 3, 1, 6, self.start_time, self.easyxf2)

        self.sheet.write(4, 0, u"结束时间：", self.easyxf9)
        self.sheet.write_merge(4, 4, 1, 6, self.start_time, self.easyxf2)

        self.sheet.write(5, 0, u"持续时间：", self.easyxf9)
        self.sheet.write_merge(5, 5, 1, 6, "0:00:00", self.easyxf2)

        self.run_case_count = 6
        self.sheet.write(self.run_case_count, 0, u"执行用例数：", self.easyxf9)
        self.sheet.write_merge(self.run_case_count, self.run_case_count, 1, 6, 0, self.easyxf2)

        self.result = 7
        self.sheet.write(self.result, 0, u"执行结果：", self.easyxf9)
        self.sheet.write_merge(self.result, self.result, 1, 6, "FAILED", self.easyxf2)



        self.sheet.write_merge(8, 8, 0, 6, "", self.easyxf7)
        self.sheet.write_merge(9, 9, 0, 6, u"用例执行情况：", self.easyxf7)
        self.sheet.write_merge(10, 10, 0, 6, "", self.easyxf7)

        row = 11
        write_list = ["禅道ID", "用例名称", "执行结果", "开始时间", "结束时间", "持续时间", "错误信息"]
        for i in write_list:
            self.sheet.write(row, write_list.index(i), i, self.easyxf5)

    def write_data(self, row,id, name, result, starttime=0, endtime=0,secondduration =0, Error=0):
        '''
        'font: height 240, name Arial, colour_index black, bold on, italic on;'
            'align: wrap on, vert centre, horiz left;'
            'borders: top NO_LINE, bottom THIN, left dashed, right double;'
            'pattern: pattern solid, fore_colour 23'
        :param row:
        :param Zentao:
        :param Name:
        :param end_time:
        :param Count:
        :param Pass:
        :param Fail:
        :param Error:
        :param Wait:
        :return:
        '''
        #self.case_count.append(Zentao)
        self.sheet.write(row, 0, id, self.easyxf4)
        self.sheet.write(row, 1, name, self.easyxf4)
        self.sheet.write(row, 2, result, self.easyxf10)
        self.sheet.write(row, 3, starttime, self.easyxf10)
        self.sheet.write(row, 4, endtime, self.easyxf10)
        self.sheet.write(row, 5, secondduration, self.easyxf10)
        self.sheet.write(row, 6, Error, self.easyxf10)
        # formula = 'IF({3}{0}>0,"Error",IF({2}{0}>0,"Fail",IF({4}{0}>0,"Wait",IF({1}{0}>0,"Pass",""))))'. \
        #     format(row + 1, chr(68), chr(69), chr(70), chr(71))
        # self.sheet.write(row, 7, Formula(formula), self.easyxf6)

        self.book.save(self.xls_file)
        #self.write_total(row + 1, endtime)

    def write_total(self, row, end_times):
        self.total_row.append(row)
        self.total_row = list(set(self.total_row))
        total_row = max(self.total_row)
        total_row_min = min(self.total_row)
        self.sheet.write(total_row, 0, "Total", self.easyxf11)
        self.sheet.write(total_row, 1, "", self.easyxf12)
        for i in range(2, 7):
            formula = 'SUM({0}{2}:{0}{1})'.format(chr(i + 65), total_row, total_row_min)
            self.sheet.write(total_row, i, Formula(formula), self.easyxf8)

        formula = 'COUNTIF(H{1}:H{0},"Pass")/COUNTA(H{1}:H{0})'.format(total_row, total_row_min)
        self.sheet.write(total_row, 7, Formula(formula), self.easyxf13)

        self.sheet.write_merge(4, 4, 1, 7, end_times, self.easyxf2)

        start_time = time.strptime(self.start_time, "%Y-%m-%d %H:%M:%S")
        end_time = time.strptime(end_times, "%Y-%m-%d %H:%M:%S")
        start_time = datetime.datetime(start_time[0], start_time[1], start_time[2],
                                       start_time[3], start_time[4], start_time[5])
        end_time = datetime.datetime(end_time[0], end_time[1], end_time[2],
                                     end_time[3], end_time[4], end_time[5])
        continue_time = end_time - start_time
        self.sheet.write_merge(5, 5, 1, 7, str(continue_time), self.easyxf2)

        formula = u'"通过 "&COUNTIF(H13:H{0},"Pass")&"； 失败 "&COUNTIF(H13:H{0},"Fail")&"； 执行错误 "&' \
                  u'COUNTIF(H13:H{0},"Error")&"； 人工检查 "&COUNTIF(H13:H{0},"Wait")&"；"'.format(total_row)
        self.sheet.write_merge(6, 6, 1, 7, Formula(formula), self.easyxf2)

        self.sheet.write_merge(7, 7, 1, 7, len(set(self.case_count)), self.easyxf2)

        self.book.save(self.xls_file)

        # 写入运行时长
        with open(r"./runTime.log", "w") as run_time:
            run_time.write(str(continue_time))

