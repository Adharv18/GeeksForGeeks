'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        if head == None:
            newNode = Node(x)
            newNode.next = None
            head = newNode
            return head
        i = head
        while i.next != None:
            i = i.next
        newNode = Node(x)
        i.next = newNode
        newNode.next = None
        return head
