class Solution:
    def valEqualToPos(self, arr):
        mg = []
        for i in range(len(arr)):
            if arr[i] == i+1:
                mg.append(i+1)
            
        return mg
