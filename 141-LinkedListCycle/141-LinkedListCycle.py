# Last updated: 2/17/2026, 7:01:31 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        seen = set()
10        current = head
11        while current:
12            if current in seen:
13                return True
14            seen.add(current)
15            current = current.next
16        return False