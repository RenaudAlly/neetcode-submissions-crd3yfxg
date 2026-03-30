class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        res = 0

        intervals.sort(key = lambda i : i[0]) # sorting intervals by start time

        # Greedy algorithm
        # Updating the prevLen to the minimum end
        prevEnd = intervals[0][1]
        for interval in intervals[1:]:
            start, end = interval[0], interval[1]

            # If there is overlapping
            if start < prevEnd:
                res += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end

        return res