class Solution:
    def isSubset(self, a, b):
        mg = True
        arr = {}
        if len(b)>len(a):
            mg = False
        for i in a:
            if i in arr:
                arr[i] += 1
            else:
                arr[i] = 1
        for i in b:
            if i not in arr:
                return False
            if arr[i] == 0:
                return False
            arr[i] -= 1
        return mg
