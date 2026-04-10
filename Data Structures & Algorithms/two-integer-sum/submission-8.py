class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # hashmap: value -> index of that value
        
        # iterate through array with index and value
        for i, n in enumerate(nums):
            diff = target - n  # complement needed to reach target
            
            # check if complement already seen
            if diff in prevMap:
                # return index of complement + current index
                return [prevMap[diff], i]
            
            # store current value with its index for future lookup
            prevMap[n] = i
        
        return  # (problem guarantees a solution, so this is rarely reached)