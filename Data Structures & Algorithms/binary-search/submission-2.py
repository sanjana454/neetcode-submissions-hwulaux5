class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0                     # start of array
        high = len(nums) - 1        # end of array

        # keep searching while range is valid
        while low <= high:

            # find middle index
            mid = (low + high) // 2

            # check if middle element is target
            if nums[mid] == target:
                return mid

            # if target is smaller → search left half
            elif target < nums[mid]:
                high = mid - 1

            # if target is larger → search right half
            else:
                low = mid + 1

        # target not found
        return -1