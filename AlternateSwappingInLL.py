''' Structure of linked list Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def pairwiseSwap(self, head):
        i = head
        j = None
        if i == None or i.next == None:
            return head
        head = i.next
        while i != None and i.next != None:
            if j != None:
                j.next = i.next
            j = i
            i = i.next
            j.next = i.next
            i.next = j
            i = j.next
        return head
