# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Dummy node acts as a fixed starting anchor for the merged list
        # It helps avoid handling the first node as a special case
        dummy = ListNode()

        # Tail pointer will always point to the last node in the merged list
        tail = dummy

        # Step 1: Traverse both lists while neither is empty
        while list1 and list2:

            # Compare current nodes of both lists
            # Attach the smaller node to the merged list
            if list1.val < list2.val:
                
                # Link tail to list1's current node
                tail.next = list1

                # Move list1 forward
                list1 = list1.next

            else:
                # Link tail to list2's current node
                tail.next = list2

                # Move list2 forward
                list2 = list2.next

            # Move tail forward after attaching a node
            tail = tail.next

        # Step 2: If list1 still has remaining nodes,
        # attach them directly (already sorted)
        if list1:
            tail.next = list1

        # Step 3: If list2 still has remaining nodes,
        # attach them directly
        elif list2:
            tail.next = list2

        # Step 4: return merged list starting from dummy.next
        # (dummy itself is not part of result)
        return dummy.next