class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""  # final encoded string
        
        for s in strs:
            # store length of string + delimiter "#" + actual string
            # helps in decoding even if string contains special characters
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []   # list to store decoded strings
        i = 0      # pointer to traverse encoded string
        
        while i < len(s):
            j = i
            
            # move j to find the delimiter "#"
            # substring s[i:j] will represent the length
            while s[j] != "#":
                j += 1
            
            # convert length substring to integer
            length = int(s[i:j])
            
            # extract the actual string using the length
            # starts right after "#" and spans 'length' characters
            res.append(s[j + 1 : j + 1 + length])
            
            # move pointer to the start of next encoded segment
            i = j + 1 + length
        
        return res