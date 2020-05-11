class Solution:
    def findCircleNum(self, M):
        size = len(M)
        visited = [0] * size

        def dfs(pos):
            for i in range(size):
                if M[pos][i] == 1 and visited[i] == 0:
                    visited[i] = 1
                    dfs(i)

        res = 0
        for i in range(size):
            if visited[i] == 0:
                res += 1
                dfs(i)
        return res


s = Solution()
s.findCircleNum([[1,1,0],
 [1,1,1],
 [0,1,1]])
