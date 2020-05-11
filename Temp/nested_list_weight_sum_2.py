
class Solution:
    def depthSumInverse(self, nestedList):
        stack = []
        d = {}
        res = 0
        for i in nestedList:
            stack.append((i, 1))
        while stack:
            x, y = stack.pop()
            if isinstance(x,int):
                if y not in d:
                    d[y] = int(x)
                else:
                    d[y] += int(x)
            else:
                for i in x:
                    stack.append((i, y + 1))
        if not d:
            l = 1
        else:
            l = max(d.keys()) + 1
        for k, v in d.items():
            res += v * (l - k)
        return res


s = Solution()
s.depthSumInverse([1, [4, [6]]])
