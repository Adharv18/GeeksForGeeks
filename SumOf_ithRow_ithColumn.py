class Solution:
    def sumOfRowCol(self,mat):
        #code here
        n = len(mat)
        m = len(mat[0])
        sumOfRows = []
        sumOfCol = []
        for i in range(n):
            summ =0
            for j in range(m):
                summ += mat[i][j]
            sumOfRows.append(summ)
        for i in range(m):
            summ =0
            for j in range(n):
                summ += mat[j][i]
            sumOfCol.append(summ)
        for i,j in zip(sumOfRows,sumOfCol):
            if i != j:
                return False
        return True
        
        
