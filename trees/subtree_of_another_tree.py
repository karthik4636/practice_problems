#https://leetcode.com/problems/subtree-of-another-tree/submissions/

class Solution:
    def isSubtree(self, s, t) -> bool:
        def help(s,t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            return  help(s.left,t.left) and help(s.right,t.right)
        if not s:return False
        return help(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)