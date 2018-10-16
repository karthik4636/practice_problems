#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_list = []
        pointer = nums[0]
        new_list.append(pointer)
        for num in nums[1:]:
            if num == pointer:
                continue
            else:
                pointer = num
                new_list.append(num)
        return new_list

    def remove_in_place(self,nums):

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                del nums[i]
        return len(nums)