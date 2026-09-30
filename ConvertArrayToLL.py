from typing import List
''' Linked List Node Structure
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def arrayToList(self, arr: List[int]) -> 'Node':
        newNode = Node(arr[0])
        head = newNode
        i = head
        count = 1
        prev = None
        while count != len(arr)-1:
            newNode = Node(arr[count])
            i.next = newNode
            prev = i
            count += 1
            i = i.next
        newNode = Node(arr[len(arr)-1])
        i.next = newNode
        newNode.next = None
        return head
