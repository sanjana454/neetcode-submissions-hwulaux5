class Solution:
    def isPalindrome(self, s: str) -> bool:
        # i → left pointer, j → right pointer
        i, j = 0, len(s) - 1
        
        # loop until pointers cross
        while i < j:
            
            # skip non-alphanumeric characters from the left
            if not s[i].isalnum():
                i += 1
            
            # skip non-alphanumeric characters from the right
            elif not s[j].isalnum():
                j -= 1
            
            # if both are valid, compare them (case-insensitive)
            elif s[i].lower() == s[j].lower():
                i += 1   # move left pointer forward
                j -= 1   # move right pointer backward
            
            # mismatch → not a palindrome
            else:
                return False
        
        # all characters matched
        return True