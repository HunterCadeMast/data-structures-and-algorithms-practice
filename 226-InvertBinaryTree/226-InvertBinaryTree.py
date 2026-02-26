# Last updated: 2/26/2026, 5:00:51 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        if not root:
10            return None
11        stack = [root]
12        while stack:
13            node = stack.pop()
14            node.left, node.right = node.right, node.left
15            if node.left:
16                stack.append(node.left)
17            if node.right:
18                stack.append(node.right)
19        return root