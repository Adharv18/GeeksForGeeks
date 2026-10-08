'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def rotate(self, head, k):
        if head == None or head.next == None:
            return head
        i = head
        n = 1
        while i.next != None:
            i = i.next
            n += 1
        k = k % n
        if k == 0:
            return head
        last = i
        i = head
        for _ in range(n - k - 1):
            i = i.next
        newHead = i.next
        last.next = head
        i.next = None
        return newHead
