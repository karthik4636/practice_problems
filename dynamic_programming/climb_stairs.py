#https://leetcode.com/problems/climbing-stairs
#Note : this is nothing but a fibonacci series
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        if n == 0 or n==1:
            return 1
        if n == 2:
            return 2
        dp[0] = 1
        dp [1] = 1
        dp [2] = 2

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]




s = Solution()
s.climbStairs(3)