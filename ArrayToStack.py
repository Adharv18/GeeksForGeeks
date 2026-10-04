class Solution:
    
    #  Push elements of an array into a stack.
    def push(self, arr):
        top = -1
        stack = []
        for i in range(len(arr)-1,-1,-1):
            stack.append(arr[i])
            top += 1
        return stack
            
    
    #  Print elements of a stack and pop them.
    def printAndPop(self, stack):
        top = len(stack)-1
        for i in range(len(stack)):
            print(stack[i],end=" ")
            top -= 1
