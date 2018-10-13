class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        k={}
        for index,num in enumerate(nums):
           k[num] = index

        for index,num in enumerate(nums):
            if target - num in k and k[target-num]!=index:
                return index,k[target-num]






nums = [3,3]
target = 6

s = Solution()
c=s.twoSum(nums,target)
d=1

