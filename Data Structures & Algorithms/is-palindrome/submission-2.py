class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""  # will store only lowercase alphanumeric characters
        
        # Step 1: clean the string
        for c in s:
            # check if character is alphanumeric (ignore spaces, punctuation, etc.)
            if c.isalnum():
                # convert to lowercase and add to new string
                newstr += c.lower()
        
        # Step 2: check if cleaned string is equal to its reverse
        # newstr[::-1] gives the reversed string
        return newstr == newstr[::-1]