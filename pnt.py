
import copy

def minimax(node, depth, isMaximizingPlayer, alpha, beta, nextNodes,nextNums,tokens,custDict,numSave,isStart): 

    if depth > tokens:
        val = Standart(node,nextNodes,isMaximizingPlayer)
        custDict[numSave][0].append(val)
        return val
    
    if isMaximizingPlayer :
        bestVal = float('-inf')
        countmax = 0
        if len(nextNums) == 0:
            ran = int(tokens)
            ran=int(ran/2)
            for i in range(ran):
                #customList=list()
                if nextNodes[i]%2 == 1:
                    newnode = nextNodes[i]
                    nxtNodes  = copy.deepcopy(nextNodes)
                    nxtNodes.remove(newnode)
                    newnums = copy.deepcopy(nextNums)
                    newnums.append(newnode)
                    print("max has taken move %d against min's %d" %(newnode,node))
                    value = 0
                    if isStart == 1:
                        numSave = newnode
                        value = minimax(newnode, depth+1, False, alpha, beta,nxtNodes,newnums,tokens,custDict,numSave,3)
                    else:
                        value = minimax(newnode, depth+1, False, alpha, beta,nxtNodes,newnums,tokens,custDict,numSave,isStart)
                    custDict[numSave][1][1]+=1
                    bestVal = max( bestVal, value) 
                    alpha = max( alpha, bestVal)
                    print("2 : max has taken move %d against min's %d" %(newnode,node))
                    print("current value of alpha = %f and beta = %f" %(alpha,beta))
                    #mydict[newnode] = custList
                    if beta <= alpha:
                        custDict[numSave][1][3]+=1
                        break
                if numSave != 0:
                    custDict[numSave][1][0]+=1
                    if depth > custDict[numSave][1][2]:
                        custDict[numSave][1][2] = depth
        else:
            for newnode in nextNodes :
                #customList=list()
                if isFactor(newnode,node):
                    nxtNodes  = copy.deepcopy(nextNodes)
                    nxtNodes.remove(newnode)
                    newnums = copy.deepcopy(nextNums)
                    newnums.append(newnode)
                    print("max has taken move %d against min's %d" %(newnode,node))
                    value = 0
                    if isStart == 1:
                        numSave = newnode
                        value = minimax(newnode, depth+1, False, alpha, beta,nxtNodes,newnums,tokens,custDict,numSave,3)
                    else:
                        value = minimax(newnode, depth+1, False, alpha, beta,nxtNodes,newnums,tokens,custDict,numSave,isStart)
                    custDict[numSave][1][1]+=1
                    bestVal = max( bestVal, value) 
                    alpha = max( alpha, bestVal)
                    print("2 : max has taken move %d against min's %d" %(newnode,node))
                    print("current value of alpha = %f and beta = %f" %(alpha,beta))
                    #mydict[newnode] = custDict
                    if beta <= alpha:
                        custDict[numSave][1][3]+=1
                        break
                else:
                    countmax+=1
                if numSave != 0:
                    custDict[numSave][1][0]+=1
                    if depth > custDict[numSave][1][2]:
                        custDict[numSave][1][2] = depth
        if countmax == len(nextNodes):
            print("max has no more moves, backtracking")
            print(nextNums)
            print("-1.0")
            custDict[numSave][0].append(-1.0)
            return -1.0
        
        return bestVal

    else :
        bestVal = float('inf')
        countmin = 0
        if len(nextNums) == 0:
            ran = int(tokens)
            ran=int(ran/2)
            for i in range(ran):
                #customList=list()
                if nextNodes[i]%2 == 1:
                    newnode = nextNodes[i]
                    nxtNodes  = copy.deepcopy(nextNodes)
                    nxtNodes.remove(newnode)
                    newnums = copy.deepcopy(nextNums)
                    newnums.append(newnode)
                    print("min has taken move %d against max's %d" %(newnode,node))
                    value = 0
                    if isStart == 2:
                        numSave = newnode
                        value = minimax(newnode, depth+1, True, alpha, beta,nxtNodes,newnums,tokens,custDict,numSave,3)
                    else:
                        value = minimax(newnode, depth+1, True, alpha, beta,nxtNodes,newnums,tokens,custDict,numSave,isStart)
                    custDict[numSave][1][1]+=1
                    bestVal = max( bestVal, value) 
                    alpha = max( alpha, bestVal)
                    print("2 : min has taken move %d against max's %d" %(newnode,node))
                    print("current value of alpha = %f and beta = %f" %(alpha,beta))
                    #mydict[newnode] = custList
                    if beta <= alpha:
                        custDict[numSave][1][3]+=1
                        break
                if numSave != 0:
                    custDict[numSave][1][0]+=1
                    if depth > custDict[numSave][1][2]:
                        custDict[numSave][1][2] = depth
        else:
            for newnode in nextNodes :
                #customList=list()
                if isFactor(newnode,node):
                    nxtNodes  = copy.deepcopy(nextNodes)
                    nxtNodes.remove(newnode)
                    newnums = copy.deepcopy(nextNums)
                    newnums.append(newnode)
                    print("min has taken move %d against max's %d" %(newnode,node))
                    value = 0
                    if isStart == 2:
                        numSave = newnode
                        value = minimax(newnode, depth+1, True, alpha, beta,nxtNodes,newnums,tokens,custDict,numSave,3)
                    else:
                        value = minimax(newnode, depth+1, True, alpha, beta,nxtNodes,newnums,tokens,custDict,numSave,isStart)
                    custDict[numSave][1][1]+=1
                    bestVal = min( bestVal, value) 
                    beta = min( beta, bestVal)
                    print("2 : min has taken move %d against max's %d" %(newnode,node))
                    print("current value of alpha = %f and beta = %f" %(alpha,beta))
                    #mydict[newnode] = custList
                    if beta <= alpha:
                        custDict[numSave][1][3]+=1
                        break
                else:
                    countmin+=1
                if numSave != 0:
                    custDict[numSave][1][0]+=1
                    if depth > custDict[numSave][1][2]:
                        custDict[numSave][1][2] = depth
        
        if countmin == len(nextNodes):
            print("min has no more moves, backtracking")
            print("1.0")
            print(nextNums)
            custDict[numSave][0].append(1.0)
            return 1.0

        return bestVal

def isFactor(val1,val2):
    if val1 % val2 == 0:
        return True
    elif val2 % val1 == 0:
        return True
    else:
        return False

def CheckPrime(quest):
    num = int(value)

    if num > 1:
        for i in range(2,num//2):
            if (num % i) == 0:
                return True
            else:
                return False
        else:
            return False

def Standart(value,nextNumbers,isMax):

    returner = 1
    if not isMax:
        returner = -1
    num = int(value)
    primeCount = 0

    if num == 1:
        if len(nextNumbers)%2==1:
            returner*=0.5
            return returner
        else: 
            returner*=-0.5
            return returner
    elif CheckPrime(num):
        for nxt in nextNumbers:
            if CheckPrime(nxt):
                primeCount+=1
        if primeCount%2==1:
            returner*=0.7
            return returner
        else:
            returner*=-0.7
            return returner
    elif len(nextNumbers)==0:
        return 0
    else:
        val = divisor(num)
        if val%2 == 1:
            returner*=0.6
            return returner
        else:
            returner*=-0.6
            return returner


def divisor(n): # taken from https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-24.php
  for i in range(n):
    x = len([i for i in range(1,n+1) if not n % i])
  return x

def SortUp(mydict,isMaximizingPlayer):
    truelist = list()
    for x,y in mydict.items():
        if len(y[0]) == 0:
            continue
        else:
            part = list()
            sum = 0
            val = float("inf")
            if isMaximizingPlayer:
                for nums in y[0]:
                    sum+=nums
                    if nums < val:
                        val = nums
            else:
                val = float("-inf")
                for nums in y[0]:
                    sum+=nums
                    if nums > val:
                        val = nums

            sum = sum/len(y[0])
            part.append(x)
            part.append(sum)
            part.append(val)
            truelist.append(part)

    return truelist

def movemapper(listing,info):
    print("Move : " + str(listing[0]))
    print("Value : " + str(listing[2]))
    print("Nodes Visited : " + str(info[1][0]))
    print("Nodes Evaluated : " + str(info[1][1]))
    print("Max Depth reached : " + str(info[1][3]))
    val = info[1][0]/(info[1][0] + info[1][2])
    print("Average Effective Branching : " + str(1/val) )
    

file = open('command.txt', 'r')
Line = file.readline()
x = Line.split()

tokens = int(x[0])
used = int(x[1])
nums = list()

totals = list()
for value in range(1,tokens+1):
    totals.append(value)
for num in range(2,used+2):
    nums.append(int(x[num]))
    totals.remove(int(x[num]))

mydict = dict()
for num in totals:
    mydict[num] = [[],[0,0,0,0]]
if len(nums) != 0:
    if len(nums)%2==0:
        minimax(nums[len(nums)-1],int(x[len(x) - 1]),True,float('-inf'),float('inf'),totals,nums,tokens,mydict,0,1)
        finalList = SortUp(mydict,True)

        holder = -100
        rememNum = 0
        counter = 0
        for listing in finalList:
            if listing[1] > holder:
                rememNum = counter
                holder = listing[1]
            counter+=1
        movemapper(finalList[rememNum],mydict[listing[0]])
    else:
        minimax(nums[len(nums)-1],int(x[len(x) - 1]),False,float('-inf'),float('inf'),totals,nums,tokens,mydict,0,2)
        finalList = SortUp(mydict,False)
        holder = 100
        rememNum = 0
        counter = 0
        for listing in finalList:
            if listing[1] < holder:
                rememNum = counter
                holder = listing[1]
            counter+=1
        movemapper(finalList[rememNum],mydict[listing[0]])
else:
    minimax(0,int(x[len(x) - 1]),True,float('-inf'),float('inf'),totals,nums,tokens,mydict,0,1)
    finalList = SortUp(mydict,True)
    holder = -100
    rememNum = 0
    counter = 0
    for listing in finalList:
        if listing[1] > holder:
            rememNum = counter
            holder = listing[1]
        counter+=1
    movemapper(finalList[rememNum],mydict[listing[0]])
