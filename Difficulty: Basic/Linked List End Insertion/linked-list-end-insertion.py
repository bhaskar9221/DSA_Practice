'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        new_node = Node(x)  # create new node
        if not head:        # if list is empty
            return new_node
        curr = head
        while curr.next:    # traverse to the last node
            curr = curr.next
        curr.next = new_node
        return head