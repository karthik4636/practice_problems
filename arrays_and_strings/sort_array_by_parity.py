#https://leetcode.com/problems/sort-array-by-parity/

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []

        for num in A:
            if num%2 == 0:
                result.insert(0,num)
            else:
                result.append(num)
        return  result


s = Solution()
s.sortArrayByParity([3,1,2,4])
b=1