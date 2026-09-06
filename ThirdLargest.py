class Solution:
    def thirdLargest(self,arr):
        arr.sort()
        if len(arr) < 3:
            return -1
        return arr[-3]
