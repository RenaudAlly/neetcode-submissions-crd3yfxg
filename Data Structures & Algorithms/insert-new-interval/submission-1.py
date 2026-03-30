class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []

        # Merges the intervals
        def merge(interval1, interval2):
            start = min(interval1[0], interval2[0])
            end = max(interval1[1], interval2[1])
            return [start, end]

        for interval in intervals:
            newIntervalStart, newIntervalEnd = newInterval[0], newInterval[1]
            start, end = interval[0], interval[1]

            # Case where the interval has already been added
            if newInterval == [-1, -1]:
                res.append(interval)
            # Case where new interval should be added before current interval
            elif newIntervalEnd < start:
                res.append(newInterval)
                res.append(interval)
                newInterval = [-1, -1] # Marking it as added
            # Case where new interval should be added after current interval
            elif newIntervalStart > end:
                res.append(interval)
            # Case where there is an overlap
            else:
                newInterval = merge(interval, newInterval)
        
        # If new interval hasn't been added yet, add it at the end
        if newInterval != [-1, -1]:
            res.append(newInterval)
        
        return res