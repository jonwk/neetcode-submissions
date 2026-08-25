"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        

        start = [i.start for i in intervals]
        end = [i.end for i in intervals]

        s, e = 0, 0
        res, count = 0, 0 

        while s < len(intervals):
            if start[s] < end[e]:
                s+=1
                count+=1
            else:
                e+=1
                count-=1
        return res


