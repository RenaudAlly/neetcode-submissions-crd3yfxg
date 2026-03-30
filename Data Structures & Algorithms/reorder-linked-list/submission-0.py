# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:  
        # Pseudocode
        # 1. Find start of the second list
        # 2. Reverse the second list
        # 3. Merge the two lists

        # Questions
        # Why do we initialize fast pointer to second node for midpoint and first mode for detecting a cycle? What is the reasoning

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Start of second list
        second = slow.next
        prev = slow.next = None

        # Reversing the second list
        while second:
            # Creating links
            ahead = second.next # Saving next node
            second.next = prev # Reversing current link
            # Iterating pointers
            prev = second
            second = ahead

        # By the end, second will point to NULL, prev will be head of the reversed list
        first, second = head, prev

        # Merging the two lists (second half can be smaller)
        while second:
            # Saving node values
            tmp1, tmp2 = first.next, second.next
            # Modifying links
            first.next = second
            second.next = tmp1
            # Updating pointers
            first, second = tmp1, tmp2            