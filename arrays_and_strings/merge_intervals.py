#https://leetcode.com/problems/merge-intervals/
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        # sort
        result = []
        intervals.sort(key=lambda i: i.start)

        for i in intervals:
            if len(result) == 0:
                result.append(i)
            if i.start <= result[-1].end and i.end > result[-1].end:
                result[-1].end = i.end
            elif i.start > result[-1].end:
                result.append(i)

        return result


s = Solution()
s.merge([[1,4],[4,5]])

