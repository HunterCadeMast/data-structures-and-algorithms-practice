# Last updated: 2/12/2026, 3:45:22 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        string = s.split(" ")
        seperated = ""
        for word in string:
            seperated = seperated + word[::-1] + " "
        return seperated.rstrip()