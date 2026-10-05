'''
structure of a linked list node 
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def insertInMiddle(self, head, x):
        newNode = Node(x)
        if head == None:
            return newNode
        count = 0
        i = head
        while i != None:
            count += 1
            i = i.next
        position = (count + 1) // 2
        j = head
        prev = None
        current = 0
        while current < position:
            prev = j
            j = j.next
            current += 1
        prev.next = newNode
        newNode.next = j
        return head
