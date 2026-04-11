class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # move left pointer until alphanumeric
            while l < r and not self.alphaNum(s[l]):
                l += 1

            # move right pointer until alphanumeric
            while l < r and not self.alphaNum(s[r]):
                r -= 1

            # compare characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False

            # move both pointers inward
            l, r = l + 1, r - 1

        return True

    def alphaNum(self, c):
        # check if character is A-Z, a-z, or 0-9 using ASCII
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )