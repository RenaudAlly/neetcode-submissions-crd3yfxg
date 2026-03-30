"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Pseudocode
        # Sort the intervals based on start times
        # Maintain an array of valid meeting times so far
        # For each interval,
        # Check if valid: start_2 >= end_1

        # O (n log n)

        # Edge case: No intervals
        if not intervals:
            return True

        intervals.sort(key = lambda i : i.start)

        meetings = [intervals[0]]

        for i in range(1, len(intervals)):
            # Getting times 
            prev_start, prev_end = meetings[-1].start, meetings[-1].end
            current_start, current_end = intervals[i].start, intervals[i].end

            # Checking if invalid
            if not current_start >= prev_end:
                return False

            meetings.append(intervals[i])

        return True 