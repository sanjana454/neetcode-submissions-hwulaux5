class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}  # frequency map for current window

        for r in range(len(s)):
            # include current character in window
            count[s[r]] = 1 + count.get(s[r], 0)

            # check if window is valid
            # replacements needed = window size - max frequency
            while (r - l + 1) - max(count.values()) > k:
                # shrink window from left
                count[s[l]] -= 1
                l += 1

            # update maximum window size
            res = max(res, r - l + 1)

        return res