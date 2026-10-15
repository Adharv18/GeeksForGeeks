class Solution:
    def reverseFirstK(self, q, k):
        
        arr = list(q)
        if len(arr) < k:
            return deque(arr)
        else:
            first_part = arr[:k][::-1]
            rem_part = arr[k:]
            final = first_part+rem_part
        return deque(final)
            
        
        
