class Solution:
    def countFreq(self, arr, target):
        tar = 0
        for i in arr:
            if i == target:
                tar = tar+1
        return tar
