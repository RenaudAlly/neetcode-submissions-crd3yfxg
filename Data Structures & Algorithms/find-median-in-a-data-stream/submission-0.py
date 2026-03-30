class MedianFinder:

    def __init__(self):
        # Max heaps are not implemented by default python. Need to use a trick
        # Small heap (containing smaller numbers) is implemented as max heap
        # Large heap (containing larger numbers) is implemted as min heap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # We want to maintain two properties
        # 1. Max value in small heap <= Min value in large heap
        # 2. The size should approximately be the same (at most difference of 1)

        # By default, we add to the small heap
        heapq.heappush(self.small, -1 * num)

        # Checking our conditions
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Handling case where small heap is larger
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # Handling case where large is larger
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # We have ensured that the heap sizes are balanced
        # Getting median depending on size
        sHeapSize, lHeapSize = len(self.small), len(self.large)

        if sHeapSize == lHeapSize:
            return (-self.small[0] + self.large[0]) / 2
        elif sHeapSize > lHeapSize:
            return -self.small[0]
        else:
            return self.large[0]         