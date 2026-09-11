class Solution:
    def modify(self, s):
        arr = list(s)
        ar = []
        pos = []
        vowels = ["a","e","o","i","u"]
        for i in range(len(arr)):
            if arr[i] in vowels:
                pos.append(i)
                ar.append(arr[i])
        ar.reverse()
        for i in range(len(ar)):
            arr[pos[i]] = ar[i]
        s = "".join(arr)
        return s
