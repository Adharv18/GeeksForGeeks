''' Structure of linked list Node
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def removeDuplicates(head):
    arr = set()
    i = head
    prev = None
    while i != None:
        if i.data in arr:
            prev.next = i.next
            i = i.next
        else:
            arr.add(i.data)
            prev = i
            i = i.next
    return head
