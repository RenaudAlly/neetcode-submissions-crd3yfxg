# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Examples: 
        # 1 -> 2 -> 4
        # 1 -> 3 -> 5

        # Pseudocode
        # 1. while both nodes exist, compare the values of the node.
        # 2. wire the nodes together in order, and increment the pointer
        #       a. Wiring together: head = bigger value. head.next = smaller node 
        # 3. attach the remaining nodes from the longer list to the end

        l1, l2 = list1, list2
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            # Comparing both nodes
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next

            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next 
        
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next