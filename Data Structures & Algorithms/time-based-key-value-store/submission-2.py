"""
Examples

for key = "alice"

(1, "happy")

"""

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        pair = (timestamp, value)
        self.store[key].append(pair)

    def get(self, key: str, timestamp: int) -> str:
        # Checking if key is in the data store or not
        if key not in self.store.keys():
            return ""
        
        # Performing binary search on the list to find most recent value
        timestamps = self.store[key]
        l = 0
        r = len(timestamps) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2

            time, value = timestamps[m]

            if time == timestamp:
                return value
            elif time < timestamp:
                res = value
                l = m + 1
            else:
                r = m - 1
        
        return res