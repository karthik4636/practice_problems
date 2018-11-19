#https://leetcode.com/problems/jewels-and-stones/
class Solution:

    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if not J or  not S:
            return 0
        count = 0
        for i in S:
            if i in J:
                count+=1
        return count



s = Solution()
s.numJewelsInStones(J = "Z", S = "zz")
b=1
