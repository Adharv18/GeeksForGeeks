"""Structure of a linked list node

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""
class Solution:

    def deleteAllOccurances(self, head, x):
        prev = None
        i = head
        while i != None:
            if i.data == x:
                if i == head:
                    head = i.next
                    i = head
                else:
                    prev.next = i.next
                    i = i.next
            else:
                prev = i
                i = i.next
        return head
