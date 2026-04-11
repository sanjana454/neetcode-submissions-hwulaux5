class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()   # stores characters in current window
        l = 0             # left pointer of window
        res = 0           # max length found
        
        # expand window using right pointer
        for r in range(len(s)):
            
            # if duplicate found, shrink window from left
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            # add current character to window
            charSet.add(s[r])
            
            # update max length of valid window
            res = max(res, r - l + 1)
        
        return res