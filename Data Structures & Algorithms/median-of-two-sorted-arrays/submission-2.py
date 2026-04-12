class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # ensuring first array is smaller one
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        n1, n2 = len(nums1), len(nums2)
        low, high = 0, n1

        # performing binary search on the smaller array
        while low <= high:
            # calculating cut points in both arrays
            cut1 = (low + high) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1

            # Handling edge elements using -inf and inf
            l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            r1 = float('inf') if cut1 == n1 else nums1[cut1]
            r2 = float('inf') if cut2 == n2 else nums2[cut2]

            # checking if partition is correct
            if l1 <= r2 and l2 <= r1:
                # even total length: take average of max left and min right
                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    # odd length: take max of left side
                    return max(l1, l2)
            elif l1 > r2:
                # move left in a[]
                high = cut1 - 1
            else:
                low = cut1 + 1

        return 0.0