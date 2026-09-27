'''Definition of a Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''

class Solution:
    def sortedInsert(self, head, key):
        newNode = Node(key)
        if key < head.data:
            newNode.next = head
            head = newNode
            return head
        prev = None
        i = head
        while i != None:
            if key < i.data:
                prev.next = newNode
                newNode.next = i
                return head
            if i.next == None:
                i.next = newNode
                newNode.next = None
                return head
            prev = i
            i = i.next
        return head
