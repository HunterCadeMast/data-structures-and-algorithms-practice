# Last updated: 2/13/2026, 7:24:30 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        for bracket in s:
5            if bracket == '(' or bracket == '{' or bracket == '[':
6                stack.append(bracket)
7            elif bracket == ')' or bracket == '}' or bracket == ']':
8                if len(stack) == 0:
9                    return False
10                if bracket == ')' and stack[-1] == '(':
11                    stack.pop()
12                elif bracket == '}' and stack[-1] == '{':
13                    stack.pop()
14                elif bracket == ']' and stack[-1] == '[':
15                    stack.pop()
16                else:
17                    return False
18        if len(stack) == 0:
19            return True
20        else:
21            return False
22