class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0                      # left pointer
        r = len(nums) - 1          # right pointer

        res = nums[0]              # store minimum found so far

        # binary search loop
        while l <= r:

            # case 1: current subarray is already sorted
            # smallest element is at left
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break  # no need to search further

            # find middle index
            m = (l + r) // 2

            # update result with middle element
            res = min(res, nums[m])

            # check which side is sorted
            if nums[m] >= nums[l]:
                # left half is sorted
                # so minimum must be in right half
                l = m + 1
            else:
                # right half is sorted
                # so minimum must be in left half (including mid)
                r = m - 1

        return res