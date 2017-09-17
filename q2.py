# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:40:43 2017

@author: danna
"""
import sys

class buffet:
    def __init__(self):
        self._dishWidth = {}
        self._dishCount = {}
        self._dishType = 0
        self._dishTotal = 0
        self._minTable = 0
        
    def dishes(self, n):
        self._dishType = n
    
    def separation(self, n):
        self._distance = n
    
    def hot(self, n):
        self._hot = n
    
    def table_width(self, n):
        self._tableWidth = n
    
    def dish_width(self, dishId, width):
        self._dishWidth[dishId] = width
    
    def demand(self, dishId, cnt):
        self._dishCount[dishId] = cnt
    
    def setTotalNumDishes(self):
        for dishId, values in self._dishCount.items():
            self._dishTotal += values

    def getMinTables(self):
        return self._minTable
    
    def calculate(self):
        spaceOccupied = self._hot # but think! dish width
        
        if self._hot > 0:
            spaceOccupied += int(self._distance)
            self._hot = 0
        else:
            self._hot = 0
        
        
        
        return 1
    

def getFuncName(inputStr):
    #inputStr = inputStr.strip() # Remove leading & ending whitespace
    inputStr = inputStr.replace(" ", "")
    func = inputStr.split('(')
    return func[0]
    
if __name__=='__main__':
    inputFileName = sys.argv[1]
    file = open(inputFileName, 'r')
    inputs = file.readlines()
    
    mybuffet = buffet()
    
    for line in inputs:
        inputs = line.split('.')
        for i in range(len(inputs)-1):
            inputStr = inputs[i].replace(" ", "")
            funcName = inputStr.split('(')
            
            if funcName[0] == 'dishes':
                getArg = funcName[1].split(')')
                mybuffet.dishes(int(getArg[0]))
            elif funcName[0] == 'separation':
                getArg = funcName[1].split(')')
                mybuffet.separation(int(getArg[0]))
            elif funcName[0] == 'hot':
                getArg = funcName[1].split(')')
                mybuffet.hot(int(getArg[0]))
            elif funcName[0] == 'table_width':
                getArg = funcName[1].split(')')
                mybuffet.table_width(int(getArg[0]))
            elif funcName[0] == 'dish_width':
                getArg = funcName[1].split(')')
                getArg = getArg[0].split(',')
                mybuffet.dish_width(int(getArg[0]), int(getArg[1]))
            elif funcName[0] == 'demand':
                getArg = funcName[1].split(')')
                getArg = getArg[0].split(',')
                mybuffet.demand(int(getArg[0]), int(getArg[1]))
            else:
                raise ValueError('Invaild Input Function name')
    
    mybuffet.setTotalNumDishes()          
    print("tables(" + str(mybuffet.getMinTables())+").")
               
            
                
            
            
            
            
            
            