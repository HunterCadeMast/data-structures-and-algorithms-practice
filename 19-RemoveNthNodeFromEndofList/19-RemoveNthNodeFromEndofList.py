# Last updated: 2/25/2026, 6:10:55 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        dummy_node = ListNode(0, head)
9        left = dummy_node
10        right = head
11        while n > 0:
12            right = right.next
13            n -= 1
14        while right:
15            left = left.next
16            right = right.next
17        left.next = left.next.next
18        return dummy_node.next