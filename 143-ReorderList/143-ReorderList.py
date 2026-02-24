# Last updated: 2/24/2026, 2:32:09 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11        slow = head
12        fast = head.next
13        while fast and fast.next:
14            slow = slow.next
15            fast = fast.next.next
16        second = slow.next
17        previous = slow.next = None
18        while second:
19            temp = second.next
20            second.next = previous
21            previous = second
22            second = temp
23        first = head
24        second = previous
25        while second:
26            temp_first = first.next
27            temp_second = second.next
28            first.next = second
29            second.next = temp_first
30            first = temp_first
31            second = temp_second