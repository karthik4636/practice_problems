#https://leetcode.com/problems/zigzag-conversion/

class Solution():
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        out = []
        for i in range(numRows):
            out.append([])
        count = 0
        down = True
        i = 0
        while i <  len(s):
            if down is True:
                while count < numRows-1 and i<len(s):
                    out[count].append(s[i])
                    count += 1
                    i+=1
                down = False

            if down is False:
                while count > 0 and i < len(s):
                    out[count].append(s[i])
                    count -=1
                    i+=1
                down = True

        d = []
        for x in out:
            for j in x:
                d.append(j)
        return "".join(d)













s = Solution()
s.convert("PAYPALISHIRING", numRows = 4)
