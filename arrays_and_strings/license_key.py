#https://leetcode.com/problems/license-key-formatting/
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        s = S.replace("-", "")
        first = len(s) % K
        new = ""
        i = 0
        if first == 0:
            first_index = K
        else:
            first_index = first
        new += s[0:first_index].upper()
        i = first_index

        while i <= len(s) - 1:

            new += "-" + (s[i:i + K]).upper()
            i = i + K

        return new


s = Solution()
s.licenseKeyFormatting(S="5", K=1)
