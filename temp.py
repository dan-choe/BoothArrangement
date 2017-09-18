
        
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
            