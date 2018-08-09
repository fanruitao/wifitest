#coding=utf-8
from  xml.dom.minidom import parse
import datetime


def base_url():
    dom = parse("./common/config.xml")
    root = dom.documentElement
    logintag = root.getElementsByTagName('login')
    baseurl = logintag[0].getAttribute("baseurl")
    return baseurl
def get_current_time():
    return
def right_password():
    # 从配置文件中获取，正确的登录密码
    dom = parse("./common/config.xml")
    root = dom.documentElement
    logintag = root.getElementsByTagName('login')
    rightpassword = logintag[0].getAttribute('rightpassword')
    return rightpassword
def wrong_password():
    #从配置文件中获取错误的登录密码
    dom = parse("./common/config.xml")
    root = dom.documentElement
    logintag = root.getElementsByTagName('login')
    wrongpassword = logintag[0].getAttribute('wrongpassword')
    return wrongpassword
def ip_address():
    #从配置文件中获取上网设置页面的IP地址
    dom = parse("./common/config.xml")
    root = dom.documentElement
    wantag = root.getElementsByTagName('wan')
    ipaddress = wantag[0].getElementsByTagName("static")[0].getAttribute("ipaddress")
    return ipaddress
def mask():
    # 从配置文件中获取上网设置页面的子网掩码
    dom = parse("./common/config.xml")
    root = dom.documentElement
    wantag = root.getElementsByTagName('wan')
    mask = wantag[0].getElementsByTagName("static")[0].getAttribute("mask")
    return mask
def gateway():
    #从配置文件中获取上网设置页面的默认网关
    dom = parse("./common/config.xml")
    root = dom.documentElement
    wantag = root.getElementsByTagName('wan')
    gateway = wantag[0].getElementsByTagName("static")[0].getAttribute("gateway")
    return gateway
def dns():
    dom = parse("./common/config.xml")
    root = dom.documentElement
    wantag = root.getElementsByTagName('wan')
    dns = wantag[0].getElementsByTagName("static")[0].getAttribute("dns1")
    return dns
def new_lan_ip():
    dom = parse("./common/config.xml")
    root = dom.documentElement
    newlanip=root.getElementsByTagName("changeIP")[0].getAttribute("ip")
    return newlanip
def original_login_password():
    dom = parse("./common/config.xml")
    root = dom.documentElement
    setup = root.getElementsByTagName("setup")
    originalpassword = setup[0].getElementsByTagName("modifypassword")[0].getAttribute("currpassword")
    return originalpassword
def new_login_password():
    dom = parse("./common/config.xml")
    root = dom.documentElement
    setup = root.getElementsByTagName("setup")
    newpassword = setup[0].getElementsByTagName("modifypassword")[0].getAttribute("newpassword")
    return newpassword
def uploadpng():
    dom = parse("./common/config.xml")
    root = dom.documentElement
    setup = root.getElementsByTagName("setup")
    uploadpng = setup[0].getElementsByTagName("updatefw")[0].getAttribute("uploadpng")
    return uploadpng
def ifsendmail():
    dom = parse(r"./common/config.xml")
    root = dom.documentElement
    ifsendmail = root.getElementsByTagName("emailaddress")[0].getAttribute("ifsendmail")
    return ifsendmail










