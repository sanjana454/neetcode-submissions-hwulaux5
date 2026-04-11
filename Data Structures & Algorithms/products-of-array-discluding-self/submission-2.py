class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result array initialized with 1s
        # will store final product for each index
        res = [1] * len(nums)

        # Step 1: prefix pass (left products)
        prefix = 1  # stores product of elements to the left
        for i in range(len(nums)):
            res[i] = prefix          # store product of all elements before i
            prefix *= nums[i]        # update prefix for next index

        # Step 2: postfix pass (right products)
        postfix = 1  # stores product of elements to the right
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix        # multiply with right-side product
            postfix *= nums[i]       # update postfix for next index

        return res