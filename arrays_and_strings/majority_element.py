#https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        size = len(nums)
        majority = size//2

        max_count = 0
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i]+=1
            if count[i] > majority:
                return i
            if  count[i] > max_count:
                max_count = count[i]

    def sort_approach(self, nums):
        nums.sort()
        previous = nums[0]
        count = 1
        size = len(nums)
        if size == 1:
            return nums[0]
        for i in range(1,size):
            if nums[i] == previous:
                count+=1
            else:
                count=1
                previous = nums[i]
            if count > size//2:
                return nums[i]












s = Solution()
s.majorityElement([2,2,1,1,1,2,2])
b=s.sort_approach(nums = [2,2,1,1,1,2,2] )
print(b)