# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            # Saving node ahead
            ahead = curr.next

            # Swapping pointers
            curr.next = prev

            # Incrementing pointers
            prev = curr
            curr = ahead
        
        return prev