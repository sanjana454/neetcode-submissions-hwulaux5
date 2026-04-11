class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0  # stores the maximum water area found so far

        l = 0  # left pointer (start of array)
        r = len(heights) - 1  # right pointer (end of array)

        # try all possible container widths using two pointers
        while l < r:

            # compute current area:
            # width = distance between pointers (r - l)
            # height = limited by shorter line (min of two heights)
            area = (r - l) * min(heights[l], heights[r])

            # update maximum area if current is larger
            res = max(res, area)

            # move the pointer pointing to the shorter line
            # because height is the limiting factor for area
            if heights[l] < heights[r]:
                l += 1   # try to find a taller left line
            else:
                r -= 1   # try to find a taller right line

        # return the maximum area found
        return res