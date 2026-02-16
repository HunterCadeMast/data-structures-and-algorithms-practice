# Last updated: 2/16/2026, 4:21:03 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        current = head
9        previous = None
10        while current is not None:
11            next_node = current.next
12            current.next = previous
13            previous = current
14            current = next_node
15        return previous