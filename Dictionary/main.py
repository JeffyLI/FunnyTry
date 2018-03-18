# -*- coding:utf-8 -*-
import dictionaryOffline as df
import dictionaryOnline  as do

def judge_pure_english(keyword):  
    return all(ord(c) < 128 for c in keyword) 

tree=df.TrieTree()
filename="dictionaryfile.txt"
tree.buildTreeByFile(filename)
tree.saveTree(filename)
search=input("input:")
while search.lower() !="q":
    search=search.lower()
    if not judge_pure_english(search):
        html,search=do.searchWord(search)
        do.print_result(html)        
        search=input("input:")
        continue
    search=do.judge_input(search)
    result=tree.search(search)
    if result=="词典没有该单词":
        response=do.searchWord(search)
        do.print_result(response)
        do.saveHtmlToFile(filename,search,response)
    else:
        print("result:",result.replace(";","\n"))
    search=input("input:")

