#https://leetcode.com/problems/reverse-words-in-a-string/

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        out = []
        last_non_white = 0
        for index,i in enumerate(s):
            if i==" ":
                    if s[index-1]!=" ":
                        out.insert(0, s[last_non_white:index])


                    continue

            if index!=0 and s[index - 1] == " ":
                last_non_white = index
        out.insert(0, s[last_non_white:])
        return " ".join(out)


    def using_split_method(self,s):
        s = s.strip().split()
        b = s[::-1]
        return " ".join(b)
















s = Solution()
print(s.reverseWords("the   sky is   blue"))
s.using_split_method("the   sky is   blue")