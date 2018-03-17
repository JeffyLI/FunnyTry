# -*- coding:utf-8 -*-
import dictionaryOffline as df
import dictionaryOnline  as do

def judge_pure_english(keyword):  
    return all(ord(c) < 128 for c in keyword) 

search=input("input:")
tree=df.TrieTree()
filename="dictionaryfile.txt"
tree.buildTreeByFile(filename)
while search.lower() !="q":
    search=search.lower()
    if not judge_pure_english(search):
        html=do.searchWord(search)
        do.print_result(html)        
        search=input("input:")
        continue
    result=tree.search(search)
    if result=="词典没有该单词":
        html=do.searchWord(search)
        do.print_result(html)
        do.saveHtmlToFile(filename,search,html)
    else:
        print(result)
    search=input("input:")

