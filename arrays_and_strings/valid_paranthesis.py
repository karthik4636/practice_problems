#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = {"{":"}","[":"]","(":")"}
        stack = []

        for bracket in s:
            if not stack and bracket not in tmp:
                return False
            if bracket in tmp:
                stack.append(bracket)
            else:
                if stack:
                    x=stack.pop()
                    if tmp[x] != bracket:
                        return False


        return not bool(stack)







s = Solution()
print(s.isValid('[()]['))
b=1