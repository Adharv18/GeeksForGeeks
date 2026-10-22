class Solution:
    def findMedian(self, arr):
        arr.sort()
        if len(arr)%2 == 0:
            return ((arr[(len(arr)//2)-1])+(arr[(len(arr)//2)]))/2
        else:
            return arr[(len(arr)//2)]
