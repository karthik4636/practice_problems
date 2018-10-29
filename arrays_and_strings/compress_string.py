#https://leetcode.com/problems/string-compression/
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 1
        prim = chars[len(chars)-1]
        last_index = len(chars)-1
        for i in range(len(chars)-2,-1,-1):
            if chars[i]==prim:
                count+=1
                continue
            if count > 1:
                chars[i+1:last_index+1]=[prim] + [str(x) for x in str(count)]
            count=1
            prim = chars[i]
            last_index = i
        if count > 1:
            chars[0:last_index+1] = [prim] + [str(x) for x in str(count)]




s = Solution()
s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
