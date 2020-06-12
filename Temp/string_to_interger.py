class Solution:
    def myAtoi(self, s):
        s = s.strip()
        if len(s) == 0:
            return 0
        if s[0] not in "-+" and not s[0].isdigit():
            return 0
        num = ""
        isDigit = False
        for ch in s:
            if isDigit and not ch.isdigit():
                break
            if ch in "-+" or ch.isdigit():
                num += ch
                isDigit = True

        sign = 1
        if num[0] in "-+":
            if num[0] == "-":
                sign = -1
            num = num[1:]

        res = 0
        for ch in num:
            res *= 10
            res += ord(ch) - ord("0")
        return max(-2 ** 31, min(res * sign, 2 ** 31 - 1))