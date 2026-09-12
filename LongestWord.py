class Solution:
    def longest(self, arr):
        max = arr[0]
        for i in range(len(arr)):
            if len(max)<len(arr[i]):
                max = arr[i]
        return max
        
        
            
            
            
            
            
        
