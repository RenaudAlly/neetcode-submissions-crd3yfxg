class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn)
        intervals.sort(key = lambda i : i[0])
        result = [intervals[0]] 

        for start, end in intervals:
            prev_end = result[-1][1]

            if start <= prev_end:
                result[-1][1] = max(end, prev_end)
            else:
                result.append([start, end])

        return result