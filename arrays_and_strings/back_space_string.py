#https://leetcode.com/problems/backspace-string-compare/

class Solution(object):

    def build(self, S):
        stack = []

        for i in S:
            if i!="#":
                stack.append(i)
            elif stack:
                stack.pop()
        return "".join(stack)

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.build(S) == self.build(T)







s = Solution()
s.backspaceCompare(S="ab###c", T = "ad#c")
