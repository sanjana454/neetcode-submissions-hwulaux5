class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case: if t is empty, no window needed
        if t == "":
            return ""

        # countT → frequency of characters in t
        # window → frequency of characters in current window
        countT, window = {}, {}

        # build frequency map for t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)  # how many chars matched vs needed
        res, resLen = [-1, -1], float("inf")  # store best window
        l = 0  # left pointer

        # expand window using right pointer
        for r in range(len(s)):
            c = s[r]

            # add current character to window
            window[c] = 1 + window.get(c, 0)

            # if this character meets required frequency → increment have
            if c in countT and window[c] == countT[c]:
                have += 1

            # when window is valid, try shrinking it
            while have == need:
                
                # update result if smaller window found
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                # remove left character from window
                window[s[l]] -= 1

                # if removing breaks requirement → reduce have
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                # move left pointer to shrink window
                l += 1

        # unpack result indices
        l, r = res

        # return smallest valid substring
        return s[l:r+1] if resLen != float("inf") else ""