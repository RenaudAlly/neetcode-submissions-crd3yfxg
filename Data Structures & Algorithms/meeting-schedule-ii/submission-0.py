"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals) 

        # Core idea
        # We want to find the max number of meetings overlapping
        res = cur = 0

        # Creating separate arrays for start and end times
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        # Two possibilties. Start time < end time, or start time >= end time.
        i = j = 0

        while i < n:
            if start[i] < end[j]:
                i += 1
                cur += 1
            else:
                j += 1
                cur -= 1

            res = max(res, cur)

        return res