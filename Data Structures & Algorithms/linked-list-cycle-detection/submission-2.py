# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Pseudocode: 
        # Using fast and slow pointers. If either pointer becomes null, we know theres no cycle
        fast, slow = head, head

        while fast and fast.next:
            # Incrementing pointers
            fast = fast.next.next
            slow = slow.next

            # Checking if equal
            if fast == slow:
                return True

        return False