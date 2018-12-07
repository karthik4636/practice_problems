#https://leetcode.com/problems/reverse-integer/
# IMP study this https://www.geeksforgeeks.org/reverse-digits-integer
# -overflow-handled/
# refer this https://stackoverflow.com/questions/7604966/maximum-and-minimum
# -values-for-ints
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        b = pow(2, 31) - 1
        # neg_b = -1 * b
        num = "{}".format(abs(x))
        rev = int(num[::-1])
        if rev > b:
            return 0
        if x < 0:
            return rev * -1
        return rev

    def reverse1(self, x):
        b = pow(2, 31) - 1
        num = abs(x)
        rev = 0
        while num != 0:
            digit = num % 10
            rev = rev * 10 + digit
            if rev > b:
                return 0
            num = num // 10
        if x < 0:
            return rev * -1
        return rev


s = Solution()
s.reverse1(123)
