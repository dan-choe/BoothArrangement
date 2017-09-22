# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 22:28:02 2017

@author: danna
"""
import sys

class Tourism:
    def __init__(self):
        self.numPeople = 0
        self.numPlace = 0
        self.numPrefer = 0
        
        self.posibbleRankings = [] # rank list
        self.requestPair = [] # hold all requested pair [[id, a, b], [], ..]
        self.personOrdercnt = {}
        
        self.violation = 0
        
    def setNumPeople(self, n):
        self.numPeople = n
        for i in range(1,n+1):
            self.personOrdercnt[i] = 0
            
    def setNumPlace(self, n):
        self.numPlace = n
        
    def setNumPreferences(self, n):
        self.numPrefer = n
    
    def setOrder(self, personID, a, b):
        self.personOrdercnt[personID] += 1
        self.requestPair.append([personID,a,b])
    
    # ex: a-b, b-c => add: a-c
    def addnewFair(self):
        for personID in range(1, self.numPeople+1):
            if self.personOrdercnt[personID] > 1:
                cnt = self.personOrdercnt[personID]
                for idx in range(len(self.requestPair)):
                    if self.requestPair[idx][0] == personID:
                        for i in range(idx,idx+cnt): # 2-> add 1,  3 -> add 2, 4 -> 3, 5 ->
                            for j in range(i, idx+cnt-1):
                                a = self.requestPair[i][1]
                                b = self.requestPair[j+1][2]
                                self.requestPair.append([personID,a,b])
                        break
    
    def checkVioration(self, arr, start, end):
        isStart = False
        isEnd = False
        
        for i in range(len(arr)):
            if arr[i] == start and not isEnd:
                isStart = True
            elif arr[i] == end and not isStart: # opposite order
                isEnd = True
                return 1
            elif isStart and arr[i] == end: # found right fair
                return 0
        return 1 # since last element can be start. it is error case
    
    
    def checkViolation(self):
        
        self.addnewFair()

        numPairs = len(self.requestPair)
        
        allpermu = self.permutation([x+1 for x in range(self.numPlace)])
        """
        for i in allpermu:
            print(i)
        """    
        numPermutation = len(allpermu)
        
        minViolation = 999 # temp
        
        for permuID in range(numPermutation):
            
            errorCase = 0
            
            for pairID in range(numPairs):
                
                result = self.checkVioration(allpermu[permuID], self.requestPair[pairID][1], self.requestPair[pairID][2])
                errorCase += result
                
            if errorCase < minViolation:
                minViolation = errorCase
                #print(allpermu[permuID], 'violation:',errorCase)
        
        return minViolation
            
        
    def permutation(self,arr):
        if not len(arr):
            return []
        if len(arr) == 1:
            return [arr]
     
        permuList = []
        for i in range(len(arr)):
           m = arr[i]
           remLst = arr[:i] + arr[i+1:]
           for p in self.permutation(remLst):
               permuList.append([m] + p)
        return permuList
    
def getFuncName(inputStr):
    #inputStr = inputStr.strip() # Remove leading & ending whitespace
    inputStr = inputStr.replace(" ", "")
    func = inputStr.split('(')
    return func[0]
    
if __name__=='__main__':
    inputFileName = sys.argv[1]
    file = open(inputFileName, 'r')
    inputs = file.readlines()
    
    tourism = Tourism()
    
    for line in inputs:
        inputs = line.split('.')
        for i in range(len(inputs)-1):
            inputStr = inputs[i].replace(" ", "")
            funcName = inputStr.split('(')
            
            if funcName[0] == 'people':
                getArg = funcName[1].split(')')
                tourism.setNumPeople(int(getArg[0]))  
            elif funcName[0] == 'preferences':
                getArg = funcName[1].split(')')
                tourism.setNumPreferences(int(getArg[0]))
            elif funcName[0] == 'places':
                getArg = funcName[1].split(')')
                tourism.setNumPlace(int(getArg[0]))
            elif funcName[0] == 'order':
                getArg = funcName[1].split(')')
                getArg = getArg[0].split(',')
                tourism.setOrder(int(getArg[0]), int(getArg[1]), int(getArg[2]))
            else:
                raise ValueError('Invaild Input Function name')
    
    #print("tables(" + str(tourism.getMinTables())+").")
    #print('\npersonOrdercnt : ', tourism.personOrdercnt, '\n')
    result = tourism.checkViolation()
    
    print("violation(" + str(result)+").")
                