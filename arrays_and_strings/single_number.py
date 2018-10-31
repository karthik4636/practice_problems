class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        while (i<=len(nums)-2):
            if nums[i]!=nums[i+1]:
               return nums[i]
            i+=2
        return nums[-1]

    def solution2(self,nums):
        return 2*sum(set(nums))- sum(nums)


s = Solution()
print(s.singleNumber([2,2,1,4,1,4,7]))
print(s.solution2([2,2,1,4,1,4,7]))