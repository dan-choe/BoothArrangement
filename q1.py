# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:23:45 2017

@author: danna
"""

import sys
import numpy as np

class Booth:
    def __init__(self, _id):
        self.boothID = _id
        self.width = 0
        self.height = 0
        self.row = 0
        self.column = 0

class boothArrange:
    def __init__(self):
        self.roomWidth = 0
        self.roomHeight = 0
        self.booths = []
        self.targetID = 0
        self.targetBooth = None
        self.destinationRow = 0
        self.destinationColumn = 0
        self.minMove = 0
        self.moved = 0
    
    def setRoom(self,w,h):
        if w < 3 or h > 20:
            return False
        self.roomHeight = h
        self.roomWidth = w
        self.roomMatrix = [[0 for i in range(self.roomHeight)] for j in range(self.roomWidth)]
    
    def setNumBooths(self,n):
        if n < 1 or n > 20:
            raise ValueError('Invaild number of booths')
        self.numBooths = n
        for i in range(1,n+1):
            self.booths.append(Booth(i))
            
    def setDimension(self,targetID,w,h):
        if targetID > self.numBooths or targetID < 1:
            raise ValueError('Invaild boothID')
        target = self.booths[targetID-1]
        target.width = w
        target.height = h
        
    def setPosition(self,targetID,w,h):
        if targetID > self.numBooths or targetID < 1:
            raise ValueError('Invaild boothID')
        target = self.booths[targetID-1]
        target.row = h
        target.column = w
    
    # set idNum on occupied space of the room matrix
    def placeAllBooths(self):
        for i in range(self.numBooths):
            target = self.booths[i]
            print(target.boothID, '(w,h) ', target.width, target.height, '(r,c) ',target.row, target.column)
            row = target.row
            column = target.column
            for y in range(target.height):
                for x in range(target.width):
                    self.roomMatrix[row][column] = target.boothID
                    column+=1
                row+=1
    
    def placeATempBooth(self,targetBoothID,des_row,des_column):
        target = self.booths[targetBoothID-1]
        #print(target.boothID, '(w,h) ', target.width, target.height, '(r,c) ',target.row, target.column)
        row = target.row
        column = target.column
        for y in range(target.height):
            for x in range(target.width):
                self.roomMatrix[row][column] = target.boothID + 100
                column+=1
            row+=1
    
    def isSuccess(self):
        if self.roomMatrix[self.destinationRow][self.destinationColumn] != self.targetID:
            return False
        return True        
        """
        for y in range(target.height):
            for x in range(target.width):
                if self.roomMatrix[row][column] != self.targetID:
                    return False
                column+=1
            row+=1
        """
        
    def printMatrix(self):
        print(np.matrix(self.roomMatrix),'\n')
            
    def setDestination(self,n,c,r):
        if self.roomMatrix[r][c] > 0:
            raise ValueError('Requested Destination is already occupied by other booth.')
        else:
            self.targetBooth = self.booths[n-1]
            self.targetID = n
            self.destinationRow = r
            self.destinationColumn = c
            #target = self.booths[n-1]
            #self.startRow = target.row
            #self.startColumn = target.column
            #self.roomMatrix[r][c] = 99
    
    # Return the number of possible move steps
    def moveOtherBooth(self,bID):
        possible = {'left':0, 'right':0, 'top':0, 'bottom':0}
        target = self.booths[bID-1]
        self.getPossibleMove(target,possible)
       
    def getPossibleMove(self,target,possible):
        row = target.row
        column = target.column
        
        # up / down
        for i in range(self.roomHeight):    
            if row >= 0 and row <= self.roomHeight-1:
                return 0
        
        # left / right
        for i in range(self.roomWidth):    
            if column >= 0 and column <= self.roomHeight-1:
                return 0
    
    """
    def find_path_dfs(maze):
        start, goal = (1, 1), (len(maze) - 2, len(maze[0]) - 2)
        stack = deque([("", start)])
        visited = set()
        graph = maze2graph(maze)
        while stack:
            path, current = stack.pop()
            if current == goal:
                return path
            if current in visited:
                continue
            visited.add(current)
            for direction, neighbour in graph[current]:
                stack.append((path + direction, neighbour))
        return "NO WAY!"
    """
    
    def dfs(self):
        stack = []
        start = (self.targetBooth.row, self.targetBooth.column)
        goal = (self.destinationRow, self.destinationColumn)
        size = (self.targetBooth.height, self.targetBooth.width)
        curr = [self.targetBooth.row, self.targetBooth.column] # r, c
        #possible = {'left':0, 'right':0, 'top':0, 'bottom':0}
        
        stack_direction = []
        #y = [row[:] for row in x]
        stack.append(self.roomMatrix)
           
        def travel(side):
            # HAVE TO EDIT FOR BIGGER BOOTH (1x1)
            if side == 0: # left
                if curr[1] == 0:
                    print("can not move to left")
                    return 0
                elif self.roomMatrix[curr[0]][curr[1]-1] != 0:
                    print("[left] already occupied")
                    return self.roomMatrix[curr[0]][curr[1]-1] * -1        # Return blocked both ID
                else:
                    self.roomMatrix[curr[0]][curr[1]-1] = self.targetID      # new left space
                    self.roomMatrix[curr[0]][curr[1]+size[0]-1] = 0          # set as empty
                    curr[1] -= 1
                    self.moved += 1
                    print(np.matrix(self.roomMatrix),'\n')
                    return 1
            elif side == 1: # right
                if curr[1] == self.roomWidth-1:
                    print("can not move to right")
                    return 0
                elif self.roomMatrix[curr[0]][curr[1]+1] != 0:
                    print("[right] already occupied")
                    return self.roomMatrix[curr[0]][curr[1]+1] * -1
                else:
                    self.roomMatrix[curr[0]][curr[1]+1] = self.targetID      # new right space
                    self.roomMatrix[curr[0]][curr[1]+size[0]-1] = 0          # set as empty
                    curr[1] += 1
                    self.moved += 1
                    print(np.matrix(self.roomMatrix),'\n')
                    return 1
            elif side == 2: # top
                if curr[0] == 0:
                    print("can not move to top")
                    return 0
                elif self.roomMatrix[curr[0]-1][curr[1]] != 0:
                    print("[top] already occupied")
                    return self.roomMatrix[curr[0]-1][curr[1]] * -1
                else:
                    self.roomMatrix[curr[0]-1][curr[1]] = self.targetID      # new top space
                    self.roomMatrix[curr[0]][curr[1]] = 0                    # set as empty
                    curr[0] -= 1
                    self.moved += 1
                    print(np.matrix(self.roomMatrix),'\n')
                    return 1
            elif side == 3: # bottom
                if curr[0] == self.roomHeight-1:
                    print("can not move to bottom")
                    return 0
                elif self.roomMatrix[curr[0]+1][curr[1]] != 0:
                    print("[bottom] already occupied")
                    return self.roomMatrix[curr[0]+1][curr[1]] * -1
                else:
                    self.roomMatrix[curr[0]+1][curr[1]] = self.targetID # new bottom space
                    self.roomMatrix[curr[0]][curr[1]] = 0                    # set as empty
                    curr[0] += 1
                    self.moved += 1
                    print(np.matrix(self.roomMatrix),'\n')
                    return 1
        
        #self.roomMatrix[0][0] = 55
        #stack.append(self.roomMatrix)
      
        while stack:
            popped = stack.pop()
            isMoved = 1 # 0 for invaild move, 1 for sucessufully moved, < 0 for blocked both ID
            # row line
            while isMoved:                
                if curr[0] < goal[0]:
                    # move Down. start travel row +  line first
                    for i in range(curr[0],self.roomHeight):
                        if curr[0] == goal[0]:
                            break
                        isMoved = travel(3)
                        if isMoved == 1:
                            stack.append(self.roomMatrix[:])
                            # print(np.matrix(self.roomMatrix),'\n')
                        elif isMoved < 0:
                            print('isMoved returned', isMoved)
                            # ADD method to move other booth to 'left or Right' 
                            return
                else:
                    # move Up
                    for i in range(curr[0],0):
                        if curr[0] == goal[0]:
                            break
                        isMoved = travel(2)
                        if isMoved == 1:
                            stack.append(self.roomMatrix[:])
                            # print(np.matrix(self.roomMatrix),'\n')
                        elif isMoved < 0:
                            print('isMoved returned', isMoved)
                            # ADD method to move other booth to 'left or Right' 
                            return
                break # found row goal
                
            # colum line  
            while isMoved:
                if curr[1] < goal[1]:
                    # start travel column +  line first
                    for i in range(curr[1],self.roomWidth):
                        if curr[1] == goal[1]:
                            break
                        isMoved = travel(1)
                        if isMoved == 1:
                            stack.append(self.roomMatrix[:])
                            # print(np.matrix(self.roomMatrix),'\n')
                        elif isMoved < 0:
                            print('isMoved returned', isMoved)
                            # ADD method to move other booth to 'top or bottom' 
                            return
                else:
                    # start travel column - line first
                    for i in range(curr[1],0):
                        if curr[1] == goal[1]:
                            break
                        isMoved = travel(0)
                        if isMoved == 1:
                            stack.append(self.roomMatrix[:])
                            # print(np.matrix(self.roomMatrix),'\n')
                        elif isMoved < 0:
                            print('isMoved returned', isMoved)
                            # ADD method to move other booth to 'top or bottom' 
                            return
                break # found column goal
                
            if self.isSuccess():
                print("FOUND SOLUTION",self.moved)
                break
                
                
    
        return
            
            
    
    def getMinSteps(self):
        return self.minMove
    
    
if __name__=='__main__':
    
    inputFileName = sys.argv[1]
    file = open(inputFileName, 'r')
    inputs = file.readlines()
    
    boothArrange = boothArrange()
    
    for line in inputs:
        inputs = line.split('.')
        for i in range(len(inputs)-1):
            inputStr = inputs[i].replace(" ", "")
            funcName = inputStr.split('(')
            
            if funcName[0] == 'room':
                getArg = funcName[1].split(')')
                getArg = getArg[0].split(',')
                boothArrange.setRoom(int(getArg[0]), int(getArg[1]))
            elif funcName[0] == 'booths':
                getArg = funcName[1].split(')')
                boothArrange.setNumBooths(int(getArg[0]))
            elif funcName[0] == 'dimension':
                getArg = funcName[1].split(')')
                getArg = getArg[0].split(',')
                boothArrange.setDimension(int(getArg[0]), int(getArg[1]), int(getArg[2]))
            elif funcName[0] == 'position':
                getArg = funcName[1].split(')')
                getArg = getArg[0].split(',')
                boothArrange.setPosition(int(getArg[0]), int(getArg[1]), int(getArg[2]))
            elif funcName[0] == 'target':
                getArg = funcName[1].split(')')
                getArg = getArg[0].split(',')
                boothArrange.setDestination(int(getArg[0]), int(getArg[1]), int(getArg[2]))
            
            else:
                raise ValueError('Invaild Input Function name')
    
    boothArrange.placeAllBooths()
    boothArrange.printMatrix()         
    
    print('start search the path')
    boothArrange.dfs()
    #print("moves(" + str(boothArrange.getMinSteps())+").")
    print("moves(" + str(boothArrange.moved)+").")
                
            
            
            
            
            
            