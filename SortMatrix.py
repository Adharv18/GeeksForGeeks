class Solution:
    def sortedMatrix(self, mat):
        # code here
        arr=[]
        k = 0
        matt = []
        n = len(mat)
        for i in range(n):
            for j in range(n):
                arr.append(mat[i][j])
        arr.sort()
        for i in range(n):
            rows=[]
            for j in range(n):
                rows.append(arr[k])
                k += 1
            matt.append(rows)
        return matt
        
