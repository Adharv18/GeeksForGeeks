""" Structure of Linked List Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def getKthFromLast(self, head, k):
        length = 0
        i = head
        while i != None:
            length += 1
            i = i.next
        if k>length:
            return -1
        j = head
        for _ in range(length-k):
            j = j.next
        return j.data
            
        
        
