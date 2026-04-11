class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert list to set for O(1) lookups
        numSet = set(nums)

        # This will store the length of the longest sequence found
        longest = 0

        # Iterate through unique numbers only (avoids duplicate work)
        for n in numSet:

            # Check if 'n' is the START of a sequence
            # A number is a start if (n - 1) does NOT exist
            # Example: for sequence [1,2,3,4], only 1 is a start
            if (n - 1) not in numSet:

                # Start counting from current number
                length = 1

                # Keep checking next consecutive numbers
                # n+1, n+2, n+3, ...
                while (n + length) in numSet:
                    length += 1

                # Update longest sequence found so far
                longest = max(longest, length)

        # Return the maximum length of consecutive sequence
        return longest