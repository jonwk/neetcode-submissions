"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        l, r = 0, 1
        while r < len(intervals):
            currFinish = intervals[l].end
            nextStart = intervals[r].start
            if nextStart < currFinish:
                return False
            else:
                l = r
                r += 1

        return True
