class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)   # for O(1) lookups
        longest = 0

        # iterate over unique elements only
        for n in numSet:
            # check if it's the start of a sequence
            if (n - 1) not in numSet:
                length = 1   # start counting from current number
                
                # count consecutive numbers
                while (n + length) in numSet:
                    length += 1
                
                # update longest sequence length
                longest = max(longest, length)

        return longest