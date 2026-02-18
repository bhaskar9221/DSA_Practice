'''
# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''
class Solution:
    def areIdentical(self, head1, head2):
        # Code here
   
        current1, current2 = head1, head2
        
        
        while current1 and current2 is not None:
            
            if current1.data != current2.data:
                return False
                
            current1 = current1.next
            current2 = current2.next
        return current1 is None and current2 is None