#https://leetcode.com/problems/backspace-string-compare/

import itertools
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

    def get_first_char(self, k):
        skip = 0
        for x in reversed(k):
            if x == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield x

    def backspaceCompare1(self, S, T):
      #o(1) space

      a=self.get_first_char(S)
      b = self.get_first_char(T)
      for x,y in itertools.zip_longest(a,b):
          if x!=y:
              return False
      return True




s = Solution()
print(s.backspaceCompare1(S="ab###c", T = "a#dc"))
