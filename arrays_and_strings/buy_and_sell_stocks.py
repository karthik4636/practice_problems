#https://leetcode.com/problems/best-time-to-buy-and-sell-stock
class Solution:


    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0
        max_sale = 0
        min1 = prices[0]
        for index,i in enumerate(prices):
            min1 = min(i,min1)
            if i > min1:
                max_sale = max(max_sale,i-min1)
        return max_sale