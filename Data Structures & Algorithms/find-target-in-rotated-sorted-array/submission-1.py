class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0                      # left pointer
        r = len(nums) - 1          # right pointer

        # binary search loop
        while l <= r:
            mid = (l + r) // 2     # find middle index

            # check if we found the target
            if nums[mid] == target:
                return mid

            # check if left half is sorted
            if nums[l] <= nums[mid]:

                # if target is NOT in the left sorted half
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1    # search right half
                else:
                    r = mid - 1    # search left half

            # otherwise, right half must be sorted
            else:

                # if target is NOT in the right sorted half
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1    # search left half
                else:
                    l = mid + 1    # search right half

        # target not found
        return -1