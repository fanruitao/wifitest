class TestCaseInfo(object):
    """description of class"""
    def __init__(self,id="",name="",result="Failed",starttime="",endtime="",secondsDuration="",errorinfo=""):
        self.id = id
        self.name = name
        self.result = result
        self.starttime = starttime
        self.endtime = endtime
        self.secondsDuration = secondsDuration
        self.errorinfo = errorinfo
    def get_case_info(self):
        return (self.id,self.name,self.result,self.starttime,self.endtime,self.secondsDuration,self.errorinfo)