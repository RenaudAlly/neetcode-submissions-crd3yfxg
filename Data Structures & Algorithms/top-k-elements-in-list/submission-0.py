class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Create int to count hashmap
        frequencies = Counter(nums)

        # 2. Create buckets (dynamic array)
        buckets = [[] for _ in range(len(nums) + 1)]

        # 3. Assigning bucket based on the count
        for num, count in frequencies.items():
            buckets[count].append(num)
        print(buckets)

        # 4. Reading bucket backwards
        frequent = []
        k_dup = k
        for bucket in reversed(buckets):
            # Reading over each bucket 
            if k_dup != 0 and bucket:
                for num in bucket:
                    frequent.append(num)
                    k_dup -= 1

        return frequent