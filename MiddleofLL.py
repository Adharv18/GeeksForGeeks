''' Linked List Node Structure
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        i = head
        j = head
        while j!=None and j.next != None:
            i = i.next
            j = j.next.next
        return i.data
