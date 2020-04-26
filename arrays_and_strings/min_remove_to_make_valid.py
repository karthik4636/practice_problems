#https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s):
        stack = []
        indices_to_remove = []
        for index,i in enumerate(s):
            if i not in ["(",")"]:
                continue
            if  i=="(":
                stack.append(index)
            elif stack and  i == ")":
                stack.pop()
            elif not stack:
                indices_to_remove.append(index)
        out = set(indices_to_remove + stack)
        b = []
        for index,i in enumerate(s):
            if index not in out:
                b.append(i)
        return "".join(b)









s = Solution()
s.minRemoveToMakeValid("lee(tcode")
s.minRemoveToMakeValid("lee(t(c)o)de)")
