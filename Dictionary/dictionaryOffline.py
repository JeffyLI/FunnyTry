# -*- coding:utf-8 -*-
#英译中词典
class TrieNode:
    def __init__(self,parent):
        self.child=[""]*26
        self.content=""
        self.letter="0"
        self.parent=parent

class TrieTree:
    def __init__(self):
        self.root=TrieNode("0");

    #去重插入
    def insert(self,word,content):
        cur_node=self.root
        word=word.lower()
        for i in range(len(word)):
            index=ord(word[i])-97
            if cur_node.child[index]=="":
                cur_node.child[index]=TrieNode(cur_node)
            cur_node=cur_node.child[index]
            cur_node.letter=word[i]
        if cur_node.content=="":
            cur_node.content=content
        else:
            print("%s is already exist!"%self.getPath(cur_node))

    def search(self,word):
        cur_node=self.root
        word=word.lower()
        for i in range(len(word)):
            index=ord(word[i])-97
            if cur_node=="":
                break
            cur_node=cur_node.child[index]
        if cur_node=="" or cur_node.content=="":
            return "词典没有该单词"
        return cur_node.content

    def buildTreeByFile(self,dictneme):
        file=open(dictneme,'r')
        for x in file.readlines():
            strlist=x.strip().split(";")
            content=""
            for i in range(1,len(strlist)):
                content+=";"+strlist[i]
            self.insert(strlist[0],content)
        file.close()


    #获取内容路径，即单词
    def getPath(self,node):
        path=""
        while node.parent!='0':
            path=node.letter+path
            node=node.parent
        return path
        
    def saveTree(self,dictname):
        file=open(dictname,'w')
        nodelist=[]
        nodelist.append(self.root)
        while len(nodelist)>0:
            cur_node=nodelist[-1]
            del nodelist[-1]
            if cur_node.content!="":
                data=self.getPath(cur_node)+cur_node.content+"\n"
                file.write(data)
            for i in range(1,27):
                if cur_node.child[-i]!="":
                    nodelist.append(cur_node.child[-i])
        file.close()
            
if __name__=="__main__":
    a=TrieTree()
    a.buildTreeByFile("word.txt")
    a.saveTree("save.txt")
    searchdata=input("input:")
    while searchdata.lower()!='q':
        print(a.search(searchdata))
        searchdata=input("input:")


                
