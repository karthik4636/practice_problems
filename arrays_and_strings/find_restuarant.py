# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        if not list1 or not list2:
            return []
        sum = None
        choices = []
        for index, res in enumerate(list1):
            if res in list2:
                index2 = list2.index(res)
                if sum is None:
                    sum = index+index2
                    choices.append(res)
                    continue
                if  index2 + index < sum:
                    choices = [res]
                    sum = index+index2
                elif index+index2 == sum:
                    choices.append(res)
                    sum = index + index2



        return choices



s = Solution()
s.findRestaurant(["Shogun","KFC"],
["Shogun","KFC"])
