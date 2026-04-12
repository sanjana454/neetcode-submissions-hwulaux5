# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # prev keeps track of reversed part (initially empty)
        prev = None
        
        # curr is the pointer we use to traverse the list
        curr = head

        # Example:
        # Input:  1 → 2 → 3 → None
        # Goal:   3 → 2 → 1 → None

        while curr:

            # Step 1: save next node (important before breaking link)
            # Example: at node 2 → save 3
            nxt = curr.next

            # Step 2: reverse pointer
            # 1 → 2 becomes 1 ← 2
            curr.next = prev

            # Step 3: move prev forward
            # prev now becomes current node
            prev = curr

            # Step 4: move curr forward using saved next
            curr = nxt

        # when loop ends, prev is the new head of reversed list
        return prev