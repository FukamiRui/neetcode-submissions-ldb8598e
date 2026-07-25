"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_table = {None: None}
        curr = head
        
        while curr:
            hash_table[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = hash_table[curr]
            copy.next = hash_table[curr.next]
            copy.random = hash_table[curr.random]
            curr = curr.next
        
        return hash_table[head]
        