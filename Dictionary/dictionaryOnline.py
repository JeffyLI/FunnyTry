# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import json
import re
import win32clipboard as w
import win32con

#获取剪切板文本内容
def getText():
    w.OpenClipboard()
    try:
        d = w.GetClipboardData(win32con.CF_TEXT)
    except:
        w.CloseClipboard()
        return "非字符串"
    w.CloseClipboard()
    return(d).decode('GBK')
    
#设置剪切板内容
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()

#如果输入为空，则读取剪切板的内容
def judge_input(content):
    if content=="":
        result=getText()
        print("Search:",result)
    else:
        result=content
    return result

#打印结果
def print_result(html):
    relink=re.compile("(.+?)&nbsp;&nbsp;")
    print("result:")
    out=""
    for x in relink.findall(html):
        if("<br" in x):
            print(out)
            out=x.split(">")[1]
        else:
            out+=x+" "
    if out=="":
        out="无法翻译该单词"
    print(out)
    print(" ")

#保存查询的结果到文件
def saveHtmlToFile(filename,content,html):
    savefile=open(filename,'a')
    relink=re.compile("(.+?)&nbsp;&nbsp;")
    out=""
    for x in relink.findall(html):
        if content!="":
            savefile.write(content)
            content=""
        if("br" in x):
            savefile.write(";"+out)
            out=x.split(">")[1]
        else:
            out+=x+" "
    if out=="":
        savefile.close()
        return
    savefile.write(";"+out+"\n")
    savefile.close()

#批量查询单词和保存结果
def save_searchs(searchfilename,savefilename):
    file=open(searchfilename,'r')
    for x in file.readlines():
        try:
            content=x.strip()
            html=searchWord(content)
            saveHtmlToFile(savefilename,content,html)
            print(content)
        except:
            print("Error in :"+x)
    file.close()
    print("finish")


def searchWord(word):
    url="http://dict-co.iciba.com/search.php"
    data={}
    data['word']=judge_input(word)
    data['submit']='提交'
    data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url, data)
    html = response.read().decode('utf-8')
    return html

if __name__ =="__main__":
    content=input("input:")
    while content.title()!="Q":
        content=judge_input(content)
        if(content=="非字符串"):
            content=input("input:")
            continue
        html=searchWord(content)
        print_result(html)
        content=input("input:")
