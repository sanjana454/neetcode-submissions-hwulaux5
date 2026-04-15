class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charSet = set()   # stores characters in current window
        # l = 0             # left pointer of window
        # res = 0           # max length found
        # # expand window using right pointer
        # for r in range(len(s)):
        #     # if duplicate found, shrink window from left
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     # add current character to window
        #     charSet.add(s[r])
        #     # update max length of valid window
        #     res = max(res, r - l + 1)
        # return res

        charset=set() # initialize and empty set 
        l = 0 # left pointer is at index[0]
        r = 0 # right pointer is at index[0]
        res = 0 # result is initialized to 0
        for r in range(len(s)): # right pointer parsing through every index of string
            while s[r] in charset: # if the element pointing to the right pointer is in the set
                charset.remove(s[l]) # remove the element pointing to the left pointer
                l+=1 # and increment the position of the left pointer by 1
            charset.add(s[r]) # and add the element pointing to the right pointer
            res = max(res,r-l+1) # pick the max between the res and the pointer difference
        return res # return the result count