# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:23:45 2017

@author: danna
"""

import sys
import numpy as np
import queue

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
        self.boothLocation = []
        self.oldBooth = []
        self.targetID = 0
        self.targetBooth = None
        self.destinationRow = 0
        self.destinationColumn = 0
        self.minMove = 0
        self.moved = 0
        self.upperbound = 0
        #self.f1 = open('log.txt', 'ab')
    
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
            self.boothLocation.append([0,0])
    
    def setUpperbound(self,n):
        self.upperbound = n
            
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
        self.boothLocation[targetID-1][0] = h
        self.boothLocation[targetID-1][1] = w
    
    # set idNum on occupied space of the room matrix
    def placeAllBooths(self):
        for i in range(self.numBooths):
            target = self.booths[i]
            #print(target.boothID, '(w,h) ', target.width, target.height, '(r,c) ',target.row, target.column)
            row = target.row
            column = target.column
            for y in range(target.height):
                for x in range(target.width):
                    self.roomMatrix[row][column] = target.boothID
                    column+=1
                row+=1
    
    def isSuccess(self):
        if self.roomMatrix[self.destinationRow][self.destinationColumn] != self.targetID:
            return False
        return True
    
    def isThisSuccess(self, matrix):
        if matrix[self.destinationRow][self.destinationColumn] != self.targetID:
            return False
        return True
    
        
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

    
    def dfs(self):
        #stack = []
        stack = queue.Queue()
        start = (self.targetBooth.row, self.targetBooth.column)
        goal = (self.destinationRow, self.destinationColumn)
        size = (self.targetBooth.height, self.targetBooth.width)
        #curr = [self.targetBooth.row, self.targetBooth.column] # r, c
        #possible = {'left':0, 'right':0, 'top':0, 'bottom':0}
        
        #stack_direction = []
        #y = [row[:] for row in x]
        stack.put([0, 0, [row[:] for row in self.roomMatrix], [row[:] for row in self.boothLocation], 0])
           
        def travel(currBooth, curr, currSize, side, room):
            # HAVE TO EDIT FOR BIGGER BOOTH (1x1)
            if side == 0: # left
                if curr[currBooth.boothID-1][1] == 0:
                    #print(currBooth.boothID,"can not move to left")
                    return 0
                elif room[curr[currBooth.boothID-1][0]][curr[currBooth.boothID-1][1]-1] <= 0 and room[curr[currBooth.boothID-1][0]][curr[currBooth.boothID-1][1]-1] != currBooth.boothID * -1:
                    for i in range(currSize[0]):
                        room[curr[currBooth.boothID-1][0]+i][curr[currBooth.boothID-1][1]-1] = currBooth.boothID
                        room[curr[currBooth.boothID-1][0]+i][curr[currBooth.boothID-1][1]+(currSize[1]-1)] = 0 #currBooth.boothID * -1 # 0
                    curr[currBooth.boothID-1][1] -= 1
                    #currBooth.column -= 1
                    self.moved += 1
                   # print(np.matrix(room),'\n')
                    return 1
                else:
                    return currBooth.boothID * -1
                    #print("[left] already occupied")
                    #return self.roomMatrix[curr[0]][curr[1]-1] * -1        # Return blocked both ID
                
            elif side == 1: # right
                #print('right',curr)
                if curr[currBooth.boothID-1][1]+currSize[1]-1 == self.roomWidth-1:
                    #print(currBooth.boothID,"can not move to right")
                    return 0
                elif room[curr[currBooth.boothID-1][0]][curr[currBooth.boothID-1][1]+currSize[1] -1 + 1] <= 0 and room[curr[currBooth.boothID-1][0]][curr[currBooth.boothID-1][1]+currSize[1] -1 + 1] != currBooth.boothID * -1:
                    for i in range(currSize[0]):
                        room[curr[currBooth.boothID-1][0]+i][curr[currBooth.boothID-1][1]+(currSize[1]-1)+1] = currBooth.boothID
                        room[curr[currBooth.boothID-1][0]+i][curr[currBooth.boothID-1][1]] = 0 #currBooth.boothID * -1 # 0
                    curr[currBooth.boothID-1][1] += 1
                    #currBooth.column += 1
                    self.moved += 1
                    #print(np.matrix(room),'\n')
                    return 1
                else:
                    return currBooth.boothID * -1
                    #print("[right] already occupied")
                    #return self.roomMatrix[curr[0]][curr[1]+currSize[1]] * -1 # who occupied?
                
      
                    
            elif side == 3: # top
                if curr[currBooth.boothID-1][0] == 0:
                    #print(currBooth.boothID,"can not move to top")
                    return 0
                
                elif room[curr[currBooth.boothID-1][0]-1][curr[currBooth.boothID-1][1]] <= 0 and room[curr[currBooth.boothID-1][0]-1][curr[currBooth.boothID-1][1]] != currBooth.boothID * -1:
                    available = True
                    if currSize[1] > 1:
                        for i in range(currSize[1]):
                            if room[curr[currBooth.boothID-1][0]-1][curr[currBooth.boothID-1][1]+i] > 0 or room[curr[currBooth.boothID-1][0]-1][curr[currBooth.boothID-1][1]+i] == currBooth.boothID * -1:
                                available = False
                        
                    if available:
                        for i in range(currSize[1]):
                            room[curr[currBooth.boothID-1][0]-1][curr[currBooth.boothID-1][1]+i] = currBooth.boothID
                            room[curr[currBooth.boothID-1][0]+(currSize[0]-1)][curr[currBooth.boothID-1][1]+i] = 0#currBooth.boothID * -1 # 0
                        curr[currBooth.boothID-1][0] -= 1
                        #currBooth.row -= 1
                        self.moved += 1
                        #print(np.matrix(room),'\n')
                        return 1
                else:
                    return currBooth.boothID * -1
                
            elif side == 2: # bottom
                if curr[currBooth.boothID-1][0] == self.roomHeight-1:
                    #print(currBooth.boothID,"can not move to bottom")
                    return 0
                
                elif room[curr[currBooth.boothID-1][0]+1][curr[currBooth.boothID-1][1]] <= 0 and room[curr[currBooth.boothID-1][0]+1][curr[currBooth.boothID-1][1]] != currBooth.boothID * -1:
                    available = True
                    if currSize[1] > 1:
                        for i in range(currSize[1]):
                            if room[curr[currBooth.boothID-1][0]+(currSize[0]-1)+1][curr[currBooth.boothID-1][1]+i] > 0 or room[curr[currBooth.boothID-1][0]+(currSize[0]-1)+1][curr[currBooth.boothID-1][1]+i] == currBooth.boothID * -1:
                                available = False
                    if available:
                        for i in range(currSize[1]):
                            room[curr[currBooth.boothID-1][0]+(currSize[0]-1)+1][curr[currBooth.boothID-1][1]+i] = currBooth.boothID
                            room[curr[currBooth.boothID-1][0]][curr[currBooth.boothID-1][1]+i] = 0 #currBooth.boothID * -1 # 0
                        curr[currBooth.boothID-1][0] += 1
                        #currBooth.row += 1
                        self.moved += 1
                        #print(np.matrix(room),'\n')
                        return 1
                else:
                    return currBooth.boothID * -1
        
        def recurseBFS(movedID, room, booths, depth, boothXY, movedOtherbooth):
            
            if self.isThisSuccess( [row[:] for row in room] ):
                #print("FOUND SOLUTION 2 ", self.moved)
                #print(np.matrix([row[:] for row in room]),'\n')
                stack.queue.clear()
                self.minMove = depth + movedOtherbooth
                return depth + movedOtherbooth
            
            #for side in range(4): # 0: Left, 1: Right, 3: Up, 2: Down
            for roomID in range(1, self.numBooths+1):

                currTarget = booths[roomID-1]
                # 0: Left, 1: Right, 2: Up, 3: Down
                for side in range(4): 
                    
                    temp = [row[:] for row in room]
                    tempXY = [row[:] for row in boothXY]
                    
                    #isMoved = travel(currTarget, [boothXY[roomID-1][0], boothXY[roomID-1][1]], [currTarget.height, currTarget.width], side, room)
                    isMoved = travel(currTarget, boothXY, [currTarget.height, currTarget.width], side, room)
                    
                    if isMoved == 1:
                        #print(currTarget.boothID,' Moved. Side:',side)
                        #print(np.matrix(room),'\n')
                  
                        # compare old stack has this matrix or not
                        isHas = False
                        for n in range(len(self.oldBooth)):
                            stackTemp = self.oldBooth[n]
                            if stackTemp == room:
                                isHas = True
                        if not isHas:
                            plusStep = 0
                            if roomID != self.targetID:
                                plusStep = 1
                            stack.put([roomID, depth+1, [row[:] for row in room], [row[:] for row in boothXY], movedOtherbooth+plusStep])
                        
                        room = [row[:] for row in temp]
                        boothXY = [row[:] for row in tempXY]
                            
                        #np.savetxt(self.f1, room, fmt='%i', delimiter=",")
                        #np.savetxt(self.f1, [[]])
        
        """
        START _ END
        """
        result = 0
        while not stack.empty() :
            #print('\n popped---------------------------------------------',stack.qsize())
            popped = stack.get()
            poppedMatrix = popped[2]
            boothXY = popped[3]
            movedOtherbooth = popped[4]
            #print(np.matrix(poppedMatrix),'\n')
            #print(np.matrix(boothXY),'\n')
            
            self.oldBooth.append([row[:] for row in poppedMatrix])  
            result = recurseBFS(popped[0], [row[:] for row in poppedMatrix], self.booths[:], popped[1], [row[:] for row in boothXY], movedOtherbooth)
            
    
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
            elif funcName[0] == 'horizon':
                getArg = funcName[1].split(')')
                boothArrange.setUpperbound(int(getArg[0]))
            else:
                raise ValueError('Invaild Input Function name')
    
    boothArrange.placeAllBooths()
    #boothArrange.printMatrix()         
    
    #print('start search the path')
    boothArrange.dfs()
    print("moves(" + str(boothArrange.getMinSteps())+").")
                
            
            
            
            
            
            