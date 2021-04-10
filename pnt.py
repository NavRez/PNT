
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
                    if isStart:
                        numSave = newnode
                        value = minimax(newnode, depth+1, False, alpha, beta,nxtNodes,newnums,tokens,custDict,numSave,False)
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
                    if isStart:
                        numSave = newnode
                        value = minimax(newnode, depth+1, False, alpha, beta,nxtNodes,newnums,tokens,custDict,numSave,False)
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
                    if isStart:
                        numSave = newnode
                        value = minimax(newnode, depth+1, True, alpha, beta,nxtNodes,newnums,tokens,custDict,numSave,False)
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
                    if isStart:
                        numSave = newnode
                        value = minimax(newnode, depth+1, True, alpha, beta,nxtNodes,newnums,tokens,custDict,numSave,False)
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
    minimax(nums[len(nums)-1],0,True,float('-inf'),float('inf'),totals,nums,tokens,mydict,0,True)
else:
    minimax(0,0,True,float('-inf'),float('inf'),totals,nums,tokens,mydict,0,True)

print("hello world")