#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def searchLinkedList(self, head, x):
        #code here
        
        current  = head
        
        while current:
            if current.data == x: return True
            
            
            current = current.next
        else: return False