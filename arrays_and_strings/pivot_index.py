#https://leetcode.com/problems/find-pivot-index/
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum = 0

        for i in range(0,len(nums)):
            right_sum = total-nums[i]-left_sum
            if right_sum == left_sum:
                return i
            left_sum+=nums[i]

        return -1



s = Solution()
a=s.pivotIndex([1, 7, 3, 6, 5, 6])
print(a)