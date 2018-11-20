#https://leetcode.com/problems/merge-intervals/
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:

    def merge2(self,x,y):
        b = None
        if y.start <= x.end:
            if y.end > x.end:
                b=y.end
            else:
                b=x.end
            return True,Interval(x.start,b)
        return False, None






    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals,key=lambda x:x.start)
        i = 0
        while i <= len(intervals)-1:
            try:
                merged, merged_interval=self.merge2(intervals[i],intervals[i+1])
                if merged:
                    del intervals[i]
                    intervals[i] = merged_interval
                else:
                    i+=2
            except IndexError:
                return intervals
        return intervals




s = Solution()
s.merge([[1,4],[4,5]])

