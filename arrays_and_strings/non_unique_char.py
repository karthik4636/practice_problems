#https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {}
        for index,i in enumerate(s):
            if i in a:
                if a[i] is True:
                    a[i] = False
                continue

            a[i] = True

        low = -1
        for item, val in a.items():
            if val is True:
                index = s.index(item)
                if low == -1:
                    low=index
                    continue
                if index < low:
                    low = index
        return low





s = Solution()
b=s.firstUniqChar("aadadaad")
print(b)