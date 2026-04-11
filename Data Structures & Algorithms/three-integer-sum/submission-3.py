class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # store final triplets
        
        nums.sort()  # sort array to use two pointers + handle duplicates easily

        # fix one number at a time
        for i, a in enumerate(nums):

            # skip duplicate fixed elements to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue

            # two pointers for remaining part of array
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]  # current triplet sum

                # if sum is too large → decrease it by moving right pointer left
                if threeSum > 0:
                    r -= 1

                # if sum is too small → increase it by moving left pointer right
                elif threeSum < 0:
                    l += 1

                else:
                    # valid triplet found
                    res.append([a, nums[l], nums[r]])

                    # move left pointer to find new combinations
                    l += 1

                    # skip duplicates for left pointer
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res