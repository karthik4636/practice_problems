#https://leetcode.com/problems/powx-n/

class Solution:

    def myPow(self,x,n):
        if n == 0:
            return 1
        if n >=0:
            return self.pow_implementation(x, n)
        else:
            b = self.pow_implementation(x, -n)
            return 1.0/b

    def pow_implementation(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==1:
            return x
        half = self.pow_implementation(x,n//2)
        if n%2 == 0:
            return half*half
        else:
            return half*half*x


s = Solution()
a=s.myPow(2.00000, -2)