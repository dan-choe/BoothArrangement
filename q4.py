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
        self.ranking = []
        
        self.requestedOrder = []
        
    def setNumPeople(self, n):
        self.numPeople = n
    
    def setNumPlace(self, n):
        self.numPlace = n
        for i in range(1, n+1):
            self.ranking.append(i) # temp values
    
    def setNumPreferences(self, n):
        self.numPrefer = n
    
    def setOrder(self, personID, a, b):
        self.requestedOrder.append([personID, a, b])
        
    def permutation(self, arr):
     
        if len(arr) == 0:
            return []
     
        if len(arr) == 1:
            return [arr]
     
        # Find the permutations for lst if there are more than 1 characters
        l = [] # empty list that will store current permutation
     
        # Iterate the input(lst) and calculate the permutation
        for i in range(len(arr)):
           m = arr[i]
     
           # Extract lst[i] or m from the list.  remLst is remaining list
           remLst = arr[:i] + arr[i+1:]
     
           # Generating all permutations where m is first element
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
                getArg = funcName[1].split(-')')
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
    
    allpermu = tourism.permutation(tourism.ranking)
    
    # Q3 (4)
    #   1-2  2-3  - 1-3  [1,2,3]
    #   2-1  1-3  - 2-3  [1,2,3]   2-1 wrong
    
    #   if new element is not in the array, make possible arrays
    #  [case 1] - correct
    #   3-4  4-1  - 3-1  [4,1,2,3] 3-4 wrong, 3-1 wrong
    #   4-3  3-2  - 4-2  [4,1,2,3] 3-2 wrong
    
    #  [case 2]
    #   3-4  4-1  - 3-1  [1,2,3,4] 4-1 wrong, 3-1 wrong
    #   4-3  3-2  - 4-2  [1,2,3,4] 4-3 wrong, 3-2 wrong, 4-2 wrong
    
    
    # Q4 correct (6)
    # 1-2 2-4 4-3         [1, 2, 4, 3]
    # 2-1 1-3     - 2-3   [1, 2, 4, 3] 2-1 wrong
    # 3-4 4-1     - 3-1   [1, 2, 4, 3] 3-4 wrong, 4-1 wrong, 3-1 wrong
    # 4-3 3-2     - 4-2   [1, 2, 4, 3] 3-2 wrong, 4-2 wrong
    
    # Q5 correct (9)
    # 1-2 2-3 3-4                  [1,2,3,4]
    # 2-3 3-4 4-1  - 2-1  2-4      [1,2,3,4]  4-1 wrong, 2-1 wrong
    # 3-4 4-1 1-2  - 3-2  3-1      [1,2,3,4]  4-1 wrong, 3-2 wrong, 3-1 wrong 
    # 4-3 3-2 2-1  - 4-2  3-1      [1,2,3,4]  4-3 wrong, 3-2 wrong, 2-1 wrong, 4-2 wrong, 3-1 wrong
    
    # Q6 correct (5)
    # 1-2 2-3 +1-3  [1,2,3] 
    # new element [4,1,2,3]   [1,4,2,3]   [1,2,4,3]
    #
    # [4,1,2,3]  -- correct
    # 4-3, 3-2, +4-2      [4,1,2,3] 3-2 wrong
    # 2-4, 4-1, +2-1      [4,1,2,3] 2-4 wrong, 2-1 wrong
    # 1-3, 3-4, +1-4      [4,1,2,3] 3-4 wrong, 1-4 wrong
    #
    # [1,4,2,3]  -- correct
    # 4-3, 3-2, +4-2      [1,4,2,3] 3-2 wrong
    # 2-4, 4-1, +2-1      [1,4,2,3] 2-4 wrong, 2-1 wrong, 4-1 wrong
    # 1-3, 3-4, +1-4      [1,4,2,3] 3-4 wrong
    #
    # [1,2,4,3]  -- correct
    # 4-3, 3-2, +4-2      [1,2,4,3] 3-2 wrong, 4-2 wrong
    # 2-4, 4-1, +2-1      [1,2,4,3] 2-1 wrong, 4-1 wrong
    # 1-3, 3-4, +1-4      [1,2,4,3] 3-4 wrong
    
    
    
    for i in allpermu:
        print(i)
    
    #print("tables(" + str(tourism.getMinTables())+").")
               
            
                