class Solution:
    def removeDuplicates(self, arr):
        ar = []
        ar.append(arr[0])
        for i in range(1,len(arr)):
            if arr[i] != ar[-1]:
                ar.append(arr[i])
        arr[:] = ar
        return arr
