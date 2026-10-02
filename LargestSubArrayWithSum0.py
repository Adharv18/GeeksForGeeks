               
                
class Solution:
    def maxLength(self, arr):
        d = {}
        sum = 0
        mg = 0

        for i in range(len(arr)):
            sum = sum + arr[i]

            if sum == 0:
                mg = i + 1

            elif sum in d:
                if i - d[sum] > mg:
                    mg = i - d[sum]

            else:
                d[sum] = i

        return mg
                    
                
        
