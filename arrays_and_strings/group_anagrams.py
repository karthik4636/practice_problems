# https://leetcode.com/problems/group-anagrams/
class Solution:

    def get_dict(self,str):
        a ={}
        for i in str:
            if i not in a:
                a[i] = 1
            else:
                a[i]+=1
        return a




    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        b = {}
        for str in strs:
            sig = self.get_dict(str)
            sig = tuple(sorted(sig.items()))
            if sig not in b:
                b[sig]=[str]
            else:
                b[sig].append(str)

        return list(b.values())


s = Solution()
a=s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
b=1