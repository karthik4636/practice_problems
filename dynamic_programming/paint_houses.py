#https://leetcode.com/problems/paint-house/
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        dp = [[0]*3 for i in range(len(costs))]
        dp[0] = costs[0]

        for i in range(1,len(costs)):
            dp[i][0] = min(dp[i-1][1],dp[i-1][2])+costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

        return min(dp[-1])


s = Solution()
s.minCost([[17,2,17],[16,16,5],[14,3,19]])















s = Solution()
s.minCost([[17,2,17],[16,16,5],[14,19,3]])