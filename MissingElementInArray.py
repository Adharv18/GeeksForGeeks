class Solution:
    def missingNum(self, arr):
        n = len(arr)+1
        sumarr1 = (n*(n+1))/2
        sumarr2 = sum(arr)
        i = int(sumarr1-sumarr2)
        return i
        
