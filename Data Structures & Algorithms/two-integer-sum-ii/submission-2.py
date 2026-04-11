class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0                      # left pointer
        j = len(numbers) - 1       # right pointer
        while i < j:
            curr_sum = numbers[i] + numbers[j]
            # if we found the target
            if curr_sum == target:
                return [i + 1, j + 1]  # 1-based indexing
            # sum too small → move left pointer right
            elif curr_sum < target:
                i += 1
            # sum too large → move right pointer left
            else:
                j -= 1