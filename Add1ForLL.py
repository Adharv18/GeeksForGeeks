''' structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def addOne(self,head):
        i = head
        prev = None
        while i != None:
            if i.data != 9:
                prev = i
            i = i.next
        if prev == None:
            newNode = Node(1)
            newNode.next = head
            head = newNode
            i = head.next
            while i!= None:
                i.data = 0
                i = i.next
            return head
        prev.data += 1
        i = prev.next
        while i != None:
            i.data = 0
            i = i.next
        return head
