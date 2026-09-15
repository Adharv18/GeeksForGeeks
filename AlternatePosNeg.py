class Solution:
    def rearrange(self,arr):
        pos = []
        neg = []
        ar = []
        for i in arr:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)
        for i in range(min(len(pos),len(neg))):
            ar.append(pos[i])
            ar.append(neg[i])
        for i in range(len(neg),len(pos)):
            ar.append(pos[i])
        for i in range(len(pos),len(neg)):
            ar.append(neg[i])
        arr[:] = ar
        return arr
