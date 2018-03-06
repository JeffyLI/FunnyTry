def n_hexadecimal(numlist,n):
    for i in range(len(numlist)):
        if numlist[i]>=n:
            numlist[i]-=n
            numlist[i+1]+=1
    return numlist

def rule(choselist):
    t2=[2,3,0,1]
    if not choselist[4]==t2[choselist[1]]:
        return False
    t3=[2,5,1,3]
    temp=t3[choselist[2]]
    t3.remove(temp)
    if not (choselist[t3[0]]==choselist[t3[1]] and choselist[t3[1]]==choselist[t3[2]] and choselist[t3[0]]!=choselist[temp]):
        return False
    t4=[[0,4],[1,6],[0,8],[5,9]]
    temp=t4[choselist[3]]
    if not (choselist[temp[0]]==choselist[temp[1]]):
        return False
    t5=[7,3,8,6]
    if not (choselist[4]==choselist[t5[choselist[4]]]):
        return False
    t6=[[1,3],[0,5],[2,9],[4,8]]
    temp=t6[choselist[5]]
    if not (choselist[temp[0]]==choselist[temp[1]] and choselist[temp[0]]==choselist[7]):
        return False
    times=[0,0,0,0]
    for i in range(len(choselist)-1):
        times[choselist[i]]+=1
    t7=[2,1,0,3]
    for i in range(4):
        if times[i]<times[t7[choselist[6]]]:
            return False
    times.sort()
    t8=[6,4,1,9]
    if abs(choselist[0]-choselist[t8[choselist[7]]])==1:
        return False
    t9=[5,9,1,8]
    if choselist[0]==choselist[5]:
        if choselist[t9[choselist[8]]]==choselist[4]:
            return False
    else:
        if choselist[t9[choselist[8]]]!=choselist[4]:
            return False
    t10=[3,2,4,1]
    if not (t10[choselist[9]]==(times[3]-times[0])):
        return False
    return True

chose=[0,0,0,0,0,0,0,0,0,0,0]
answerlist=[]
letter=['A','B','C','D']
while chose[-1]==0:
    chose[0]+=1
    n_hexadecimal(chose,4)
    if rule(chose):
        temp=[]
        for i in range(len(chose)-1):
            temp.append(letter[chose[i]])
        answerlist.append(temp)
for answer in answerlist:
    print(answer)
print("Finish")
