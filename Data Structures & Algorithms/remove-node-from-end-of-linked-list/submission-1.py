# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Pseudocode
        # 1. Find length of linked list
        # 2. Calculate position to remove node
        # 3. Delete the node
        size = 0 # length of list

        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        i, pos = 1, size - n + 1 # position in linked list we want to delete

        prev, curr = None, head
        while curr and i < pos:
            prev = curr
            curr = curr.next
            i += 1

        # curr has reached position for node to delete
        
        # Edge case: Deleting first node in linked list
        if pos == 1:
            head = curr.next
            curr.next = None
            return head

        prev.next = curr.next
        curr.next = None

        return head