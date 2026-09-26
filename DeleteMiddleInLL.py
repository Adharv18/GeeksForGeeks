""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def deleteMid(self, head):
        arr = set()
        i = head
        if i.next == None:
            return None
        count = 0
        while i != None:
            count += 1
            i = i.next
        if count%2 == 0:
            count = (count/2)+1
        else:
            count = (count//2)+1
        i = head
        x = 1
        prev = None
        while x != count:
            prev = i
            i = i.next
            x += 1
        prev.next = i.next
        return head
