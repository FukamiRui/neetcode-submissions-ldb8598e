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
        curr = head
        visit = {None: None}

        while curr:
            visit[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = visit[curr]
            copy.next = visit[curr.next]
            copy.random = visit[curr.random]
            curr = curr.next
        return visit[head]
        