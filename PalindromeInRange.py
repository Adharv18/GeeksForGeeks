class Solution:
    def printPalindromes(self, m, n):
        ans = []
        for i in range(m,n+1):
            i = str(i)
            if i == i[::-1]:
                ans.append(i)
        return ans
