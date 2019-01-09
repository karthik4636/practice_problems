#https://leetcode.com/problems/fibonacci-number/

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1

        a, b = 0, 1
        for i in range(2, N + 1):
            c = a + b
            a, b = b, c
        return c

