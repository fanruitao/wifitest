from xml.etree import ElementTree as ET
from datetime import datetime
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


def easy_xf():
    easyxf1 = easyxf(
        u'font: height 320, name 宋体, colour_index 70, bold on; align: wrap on, vert top, horiz left; borders: top thin, left thin, right thin;')

    easyxf2 = easyxf(
        u'font: height 220, name 宋体; align: wrap on, horiz left; borders: right thin;')

    easyxf3 = easyxf(
        u'font: height 220, name 宋体; align: wrap on; borders: left thin, right thin;')

    easyxf4 = easyxf(
        u'font: height 220, name 宋体; align: wrap on, horiz left; borders: top thin, bottom thin, left thin, right thin; pattern: pattern solid, fore_colour 22')

    easyxf5 = easyxf(
        u'font: height 220, name 宋体, colour_index white, bold on; align: wrap on, horiz left; borders: left thin, right thin; pattern: pattern solid, fore_colour 23')

    easyxf6 = easyxf(
        u'font: height 220, name 宋体; align: wrap on, horiz centre; borders: top thin, bottom thin, left thin, right thin; pattern: pattern solid, fore_colour 22')

    easyxf7 = easyxf(
        u'font: height 220, name 宋体; align: wrap on, horiz left; borders: left thin, right thin;')

    easyxf8 = easyxf(
        u'font: height 220, name 宋体; align: wrap on; borders: top thin, bottom thin, left thin, right thin;')

    easyxf9 = easyxf(
        u'font: height 220, name 宋体, bold on; align: wrap on, horiz left; borders: left thin;')

    easyxf10 = easyxf(
        u'font: height 220, name 宋体; align: wrap on, horiz right; borders: top thin, bottom thin, left thin, right thin; pattern: pattern solid, fore_colour 22')

    easyxf11 = easyxf(
        u'font: height 220, name 宋体, bold on; align: wrap on, horiz left; borders: top thin, bottom thin, left thin;')

    easyxf12 = easyxf(
        u'font: height 220, name 宋体, bold on; align: wrap on, horiz left; borders: top thin, bottom thin, right thin;')

    easyxf13 = easyxf(
        u'font: height 220, name 宋体; align: wrap on, horiz centre; borders: top thin, bottom thin, left thin, right thin;',
        num_format_str="0%")
    return [easyxf1,easyxf2,easyxf3,easyxf4,easyxf5,easyxf6,easyxf7,easyxf8,easyxf9,easyxf10,easyxf11,easyxf12,easyxf13]

def check_path():
    current_time = time.strftime("%Y-%m-%d_%H.%M")
    path = r"./report/%s" % current_time
    # if os.path.exists(parent_path) is False:
    #     try:
    #         os.makedirs(parent_path)
    #     except OSError:
    #         import traceback
    #         print (traceback.format_exc())
    xls_file = r"%s.xls" % (path)
    return xls_file

def write_title(xlsfile):
    book=Workbook(encoding='utf-8')
    sheet = book.add_sheet("testreport", cell_overwrite_ok=True)

    sheet.col(0).width = 256 * 15
    sheet.col(1).width = 256 * 50
    sheet.col(2).width = 256 * 10
    for i in range(3, 6):
        sheet.col(i).width = 256 * 25
    sheet.col(6).width = 256 * 25

    sheet.write_merge(0, 1, 0, 6, "测试报告", easy_xf()[0])
    sheet.write_merge(2, 2, 0, 6, "", easy_xf()[2])

    teststart_time = time.strftime("%Y-%m-%d %H:%M:%S")
    sheet.write(3, 0, "开始时间：", easy_xf()[8])
    sheet.write_merge(3, 3, 1, 6, teststart_time, easy_xf()[1])

    sheet.write(4, 0, u"结束时间：", easy_xf()[8])
    sheet.write_merge(4, 4, 1, 6, teststart_time, easy_xf()[1])

    sheet.write(5, 0, u"持续时间：", easy_xf()[8])
    sheet.write_merge(5, 5, 1, 6, "0:00:00", easy_xf()[1])

    run_case_count = 6
    sheet.write(run_case_count, 0, u"执行用例数：", easy_xf()[8])
    sheet.write_merge(run_case_count, run_case_count, 1, 6, 0, easy_xf()[1])

    result = 7
    sheet.write(result, 0, u"执行结果：", easy_xf()[8])
    sheet.write_merge(result, result, 1, 6, "FAILED", easy_xf()[1])



    sheet.write_merge(8, 8, 0, 6, "", easy_xf()[6])
    sheet.write_merge(9, 9, 0, 6, u"用例执行情况：", easy_xf()[6])
    sheet.write_merge(10, 10, 0, 6, "", easy_xf()[6])

    row = 11
    write_list = ["禅道ID", "用例名称", "执行结果", "开始时间", "结束时间", "持续时间", "错误信息"]
    for i in write_list:
        sheet.write(row, write_list.index(i), i, easy_xf()[4])
    book.save(xlsfile)
    return teststart_time



    # return sheet,book

def write_data(sheet,allteststarttime, row,id, name, result, starttime=0, endtime=0,secondduration =0, Error=0):
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

    sheet.write(row, 0, id, easy_xf()[3])
    sheet.write(row, 1, name, easy_xf()[3])
    sheet.write(row, 2, result, easy_xf()[9])
    sheet.write(row, 3, starttime, easy_xf()[9])
    sheet.write(row, 4, endtime, easy_xf()[9])
    sheet.write(row, 5, secondduration, easy_xf()[9])
    sheet.write(row, 6, Error, easy_xf()[9])
    #写报告头的结束时间
    sheet.write(4,1,endtime,easy_xf()[1])
    #写报告头的持续时间

    h=str(datetime.strptime(endtime, "%Y-%m-%d %H:%M:%S") \
        - datetime.strptime(allteststarttime, "%Y-%m-%d %H:%M:%S"))
    sheet.write(5, 1, h, easy_xf()[1])
    #写执行用例数
    t=row-11
    sheet.write(6,1,t,easy_xf()[1] )
    formula = 'COUNTIF(C13:C{0},"Pass")&" Pass,"&COUNTIF( C13:C{0},"Fail")&" Fail,"&COUNTIF(C13:C{0},"error")&" Error")'.format(
        row+1)
    sheet.write(7, 1, Formula(formula), easy_xf()[1])






    # formula = 'IF({3}{0}>0,"Error",IF({2}{0}>0,"Fail",IF({4}{0}>0,"Wait",IF({1}{0}>0,"Pass",""))))'. \
    #     format(row + 1, chr(68), chr(69), chr(70), chr(71))
    # self.sheet.write(row, 7, Formula(formula), self.easyxf6)

    # book.save(xls_file)
    #self.write_total(row + 1, endtime)
def write_totalresult(sheet,row):
    formula='COUNTIF(C12:C{0},"Pass")&"Pass,"&COUNTIF( C12:C{0},"Fail")&"Fail,"&COUNTIF(C12:C{0},"error")&"Error,")'.format(row)





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

