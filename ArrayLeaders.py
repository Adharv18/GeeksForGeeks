class Solution:
    def leaders(self, arr):
        n = len(arr)
        ar = []
        right = arr[n - 1]
        ar.append(right)
        for i in range(n - 2, -1, -1):
            if arr[i] >= right:
                ar.append(arr[i])
                right = arr[i]
        ar.reverse()
        arr[:] = ar
        return arr
