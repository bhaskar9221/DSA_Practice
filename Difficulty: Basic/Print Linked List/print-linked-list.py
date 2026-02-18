
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    def displayList(self, head):
        # code here
        result = []
        current = head
        while current:
            result.append(current.data)
            current = current.next
        return result