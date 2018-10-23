#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        first = -1
        for index,i in enumerate(nums):
            if i!=target:
                continue
            if i not in seen:
                first = index
            seen[i] = index

        return [first,seen.get(target,-1)]




s = Solution()
s.searchRange(nums = [], target = 8)
