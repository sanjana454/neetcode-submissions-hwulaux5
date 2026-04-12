from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []              # stores final answers (max of each window)
        q = deque()              # monotonic deque storing INDICES (not values)

        l = r = 0                # left and right pointers of sliding window

        # move right pointer across array
        while r < len(nums):

            # STEP 1: Maintain decreasing order in deque
            # remove all indices whose values are smaller than current element
            # because they can NEVER be the maximum again
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # add current index to deque
            q.append(r)

            # STEP 2: Remove elements that are OUT of the window
            # window is [l, r], size k
            # if front index is out of window, remove it
            if q[0] < l:
                q.popleft()

            # STEP 3: If window size is valid, record answer
            if (r + 1) >= k:
                # q[0] is always index of maximum element in current window
                output.append(nums[q[0]])

                # move left pointer (window slides forward)
                l += 1

            # move right pointer
            r += 1

        return output