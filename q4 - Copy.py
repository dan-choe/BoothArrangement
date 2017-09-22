# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 22:28:02 2017

@author: danna
"""
import sys
import queue

class Tourism:
    def __init__(self):
        self.numPeople = 0
        self.numPlace = 0
        self.numPrefer = 0
        
        self.ranking = [] # rank list
        self.requestedOrder = queue.Queue() # order queue
        self.newRankList = queue.Queue()
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
        self.requestedOrder.put([personID, a, b])
        self.personOrdercnt[personID] += 1
        
    def setInitialRanking(self):
        if not len(self.ranking):
            firstOne = self.requestedOrder.get()
            self.personOrdercnt[firstOne[0]] -= 1
            if firstOne[1] not in self.ranking:
                self.ranking.append(firstOne[1])
            if firstOne[2] not in self.ranking:
                self.ranking.append(firstOne[2])
                   
            #print('num orders: ',self.personOrdercnt[firstOne[0]])
            numOrder = self.personOrdercnt[firstOne[0]]
            for i in range(numOrder):
                firstOne = self.requestedOrder.get()
                self.personOrdercnt[firstOne[0]] -= 1
                #print(firstOne[0], 'id->', i)
                if firstOne[1] not in self.ranking:
                    self.ranking.append(firstOne[1])
                if firstOne[2] not in self.ranking:
                    self.ranking.append(firstOne[2])
                
            print('Initial Ranking : ',self.ranking)
            print('Initial Ordercnt : ', tourism.personOrdercnt, '\n')
    
    # < 0 : vioration, 0: found, 1: new element
    def checkVioration(self, arr, start, end, errorCase):
        foundError = 0
        isStart = False
        isEnd = False
        
        for i in range(len(arr)):
            if arr[i] == start and not isEnd:
                isStart = True
            elif arr[i] == end and not isStart: # opposite order
                isEnd = True
                if start in self.ranking:
                    foundError -= 1
                    errorCase += 1
                    print('error', start, end)                    
            elif isStart and arr[i] == end: # found right fair
                #print('found')
                return [0, 0]
        
        # self.newRankList
        if not isStart and not isEnd: # new element
            print('new element fair',start, end)
            return [1, 0]
        elif not isStart and isEnd and foundError>=0:
            print('new start element',start, end)
            return [2, 0]
        elif isStart and not isEnd and foundError>=0:
            print('new end element ',start, end)
            return [3, 0]
        
        return [-1, errorCase]
    
    def checkRanking(self):
        arr = self.ranking[:]
        
        while not self.requestedOrder.empty():
            print('Ordercnt : ', tourism.personOrdercnt, '\n')
            
            errorCase = 0
            nextOne = self.requestedOrder.get()
            newfair = []
            # generate new fair [leftmost, rightmost]
            if self.personOrdercnt[nextOne[0]] > 1:
                newfair.append(nextOne[1])
            
            self.personOrdercnt[nextOne[0]] -= 1
            #print(nextOne[0],'current orders: ',self.personOrdercnt[nextOne[0]])
            
            result = self.checkVioration(arr[:], nextOne[1], nextOne[2], errorCase)
            if result[0] < 0:
                errorCase += 1
                #self.violation += 1
            elif result[0] == 0:
                print('------------------------perfect')
            elif result[0] == 1:
                # new fair
                self.ranking = self.ranking + [nextOne[1], nextOne[2]]
            elif result[0] == 2:
                # new start element 
                for end in range(len(self.ranking)):
                    if self.ranking[end] == nextOne[2]:
                         tempFirst = self.ranking[:end]
                         tempBack = self.ranking[end:]
                         tempFirst.append(nextOne[1])
                newLists = self.permutation(tempFirst)
                for newlist in newLists:
                    self.newRankList.put(newlist + tempBack)
                    print(newlist + tempBack)
            elif result[0] == 3:
                # new end element
                for start in range(len(self.ranking)):
                    if self.ranking[start] == nextOne[1]:
                         tempFirst = self.ranking[:start+1]
                         tempBack = self.ranking[start+1:]
                         tempBack.append(nextOne[2])
                newLists = self.permutation(tempBack)
                for newlist in newLists:
                    self.newRankList.put(tempFirst + newlist)
                    print(tempFirst + newlist)
                    
            numOrder = self.personOrdercnt[nextOne[0]]
            for i in range(numOrder):
                nextOne = self.requestedOrder.get()
                self.personOrdercnt[nextOne[0]] -= 1
                
                if self.personOrdercnt[nextOne[0]] == 0 and len(newfair)>0:
                    newfair.append(nextOne[2])
                
                #print(nextOne[0],'current orders: ',self.personOrdercnt[nextOne[0]])
                #result = self.checkVioration(nextOne[1], nextOne[2])
                result = self.checkVioration(arr[:], nextOne[1], nextOne[2], errorCase)
                
                if result[0] <0:
                    self.violation += 1
                elif result[0] == 0:
                    print('------------------------perfect')
                elif result[0] == 1:
                    # new fair
                    self.ranking = self.ranking + [nextOne[1], nextOne[2]]
                elif result[0] == 2:
                    # new start element 
                    for end in range(len(self.ranking)):
                        if self.ranking[end] == nextOne[2]:
                             tempFirst = self.ranking[:end]
                             tempBack = self.ranking[end:]
                             tempFirst.append(nextOne[1])
                    newLists = self.permutation(tempFirst)
                    for newlist in newLists:
                        self.newRankList.put(newlist + tempBack)
                        print(newlist + tempBack)
                elif result[0] == 3:
                    # new end element
                    for start in range(len(self.ranking)):
                        if self.ranking[start] == nextOne[1]:
                             tempFirst = self.ranking[:start+1]
                             tempBack = self.ranking[start+1:]
                             tempBack.append(nextOne[2])
                    newLists = self.permutation(tempBack)
                    for newlist in newLists:
                        self.newRankList.put(tempFirst + newlist)
                        print(tempFirst + newlist)
            self.personOrdercnt[nextOne[0]] = 0
            
            # there will be no need to add new fair
            if len(newfair):
                #result = self.checkVioration(newfair[0], newfair[1])
                result = self.checkVioration(arr[:], newfair[0], newfair[1], errorCase)
                if result[0] <0:
                    self.violation += 1
                print('here',newfair[0], newfair[1],'result: ',result)
    
    def permutation(self,arr):
        if not len(arr):
            return []
        if len(arr) == 1:
            return [arr]
     
        l = []
        for i in range(len(arr)):
           m = arr[i]
           remLst = arr[:i] + arr[i+1:]
           for p in self.permutation(remLst):
               l.append([m] + p)
        return l
    
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
    
    #allpermu = tourism.permutation(tourism.ranking)
    #for i in allpermu:
    #    print(i)
    
    #print("tables(" + str(tourism.getMinTables())+").")
    print('\npersonOrdercnt : ', tourism.personOrdercnt, '\n')
    tourism.setInitialRanking()
    tourism.checkRanking()
    print("violation(" + str(tourism.violation)+").")
                