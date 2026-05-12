'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    def getCount(self, head):
        # code here
        if head is None:
            return 0
        return 1 + self.getCount(head.next)