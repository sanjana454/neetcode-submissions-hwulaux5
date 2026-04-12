class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)      # total number of elements
        res = []           # final result (all subsets)
        sol = []           # current subset being built

        # backtracking function
        def backtrack(i):
            # base case: if we've considered all elements
            if i == n:
                # append a COPY of current subset
                res.append(sol[:])
                return 

            # choice 1: do NOT include nums[i]
            backtrack(i + 1)

            # choice 2: include nums[i]
            sol.append(nums[i])

            backtrack(i + 1)

            # backtrack → remove last element to explore other choices
            sol.pop()
        
        # start from index 0
        backtrack(0)

        return res