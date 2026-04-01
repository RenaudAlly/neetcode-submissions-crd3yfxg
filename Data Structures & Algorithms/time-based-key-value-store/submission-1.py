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

        
        timestamps = self.store[key]
        # Failed to find a timestamp equal to given time, just return most recent one
        r = len(timestamps) - 1
        while r >= 0:
            time, value = timestamps[r]

            if time <= timestamp:
                return value
            
            r -= 1
        
        # Failed to find even a recent value
        return ""
