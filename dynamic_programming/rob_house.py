class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        if size == 2:
            return max(nums[0],nums[1])

        max_till_now = [0]*size
        max_till_now[0] = nums[0]
        max_till_now[1] = max(nums[0],nums[1])

        for i in range(2,size):
            max_till_now[i] = max(max_till_now[i-1],nums[i]+max_till_now[i-2])

        return max_till_now[-1]





s = Solution()
s.rob([2,1,1,2])