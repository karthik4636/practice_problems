class Solution:
    def findMinDifference(self, timePoints):
        result = []
        for i in timePoints:
            hour, minute = i.split(':')
            x = int(hour)*60 + int(minute)
            result.append(x)
        result.sort()
        result.append(result[0])
        output = float('inf')
        for i in range(1,len(result)):
            diff = abs(result[i]-result[i-1])
            output = min(output,diff,(24*60)-diff)
        return output