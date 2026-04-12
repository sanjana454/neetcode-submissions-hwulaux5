# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow pointer moves 1 step at a time
        slow = head

        # fast pointer moves 2 steps at a time
        fast = head

        # traverse while fast can move ahead safely
        while fast and fast.next:

            # move slow by 1 step
            slow = slow.next

            # move fast by 2 steps
            fast = fast.next.next

            # if they meet → cycle exists
            if slow == fast:
                return True

        # if fast reaches end → no cycle
        return False        