""" Structure of Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        current = head
        prev = None
        while current != None:
            new = current.next
            current.next = prev
            prev = current
            current = new
        return prev
        
