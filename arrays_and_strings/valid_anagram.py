#https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def get_sig(self, s):
        a = {}
        for i in s:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        return a

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        a = self.get_sig(s)
        b = self.get_sig(t)
        return a == b


