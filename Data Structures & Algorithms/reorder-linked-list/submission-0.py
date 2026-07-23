# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None

        stack = deque()
        curr = head.next

        while curr:
            stack.append(curr)
            curr = curr.next
        
        curr = head
        while stack:
            curr.next = stack.pop()
            curr = curr.next

            if stack:
                curr.next = stack.popleft()
                curr = curr.next
        curr.next = None

        