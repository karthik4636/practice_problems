#https://leetcode.com/problems/nested-list-weight-sum/
class Solution(object):

    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def recursive(nestedList,depth):
            s=0
            for item in nestedList:
                if isinstance(item,int):
                    s+=int(item)*depth
                else:
                    s+=recursive(item,depth+1)
            return s
        return recursive(nestedList,1)

s = Solution()
print(s.depthSum( [1,[4,[6]]]))