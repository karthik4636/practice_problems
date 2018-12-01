#https://leetcode.com/problems/maximum-subarray/submissions/
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max = nums[0]
        max_so_far = nums[0]
        l, r = 0, 0
        for i in range(1, len(nums)):
            tmp = current_max + nums[i]
            if nums[i] > tmp:
                current_max = nums[i]
                l = i
            else:
                current_max = tmp
            if current_max > max_so_far:
                max_so_far = current_max
                r = i

            # current_max = max(nums[i],current_max + nums[i])
            # max_so_far = max(max_so_far, current_max)

        return max_so_far


s = Solution()
s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
