# -*- coding: utf-8 -*-
import urllib.request
import urllib
import json
import re
import socket

def print_result(ip,country,region,city,isp):
    print("查询ip:",ip)
    print("地区:",country,region,city)
    print("运营商:",isp)

def Get_response(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    return json.loads(html)    

def Get_selfip():
    url='http://2017.ip138.com/ic.asp'
    response = urllib.request.urlopen(url)
    html = response.read().decode('gb2312')
    result=re.compile('\[(.+?)\]')
    for x in result.findall(html):
        return x

def taobao_response(ip):
    try:
        url="http://ip.taobao.com/service/getIpInfo.php?ip="+ip
        data=Get_response(url)
        data2=data['data']
        print("Taobao Response:")
        print_result(data2['ip'],data2['country'],data2['region'],data2['city'],data2['isp'])
    except:
        print("Taobao Fail")
    
def sina_response(ip):
    try:
        url="http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip="+ip
        data=Get_response(url)
        print("Sina Response:")
        print_result(ip,data['country'],data['province'],data['city'],data['isp'])
    except:
        print("Sina Fail")

#http://2017.ip138.com/ic.asp
#http://ip.taobao.com/service/getIpInfo.php?ip=10.242.28.229
#http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=59.37.164.179
print('当前主机名称为 : ' + socket.gethostname())
print('当前主机的IP为: ' + socket.gethostbyname(socket.gethostname()))
print("本机外网ip:",Get_selfip())
ip=input('Please input the ip address:')
taobao_response(ip)
sina_response(ip)
