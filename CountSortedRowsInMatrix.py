class Solution:
    def sortedCount(self, mat: list[list[int]]) -> int:
        count = 0
        for i in range(n):
            arr = []
            newArr = []
            for j in range(m):
                arr.append(mat[i][j])
            newArr[:] = arr
            arr.sort()
            if newArr == arr:
                count += 1
        return count
