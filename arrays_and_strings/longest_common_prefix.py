class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        length = min([len(x)for x in strs])
        prefix = ""
        for i in range(0,length):
            for j,a in enumerate(strs):
                if j==0:
                    tmp = a[i]
                    continue
                if tmp != a[i]:
                    return prefix

            prefix+=tmp

        return prefix








s = Solution()
c=s.longestCommonPrefix(["","",""])
b=1