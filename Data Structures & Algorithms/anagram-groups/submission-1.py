class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # map: char count tuple -> list of anagrams
        
        for s in strs:
            count = [0] * 26  # frequency array for 26 lowercase letters
            
            for c in s:
                # increment count for each character
                count[ord(c) - ord("a")] += 1
            
            # use tuple(count) as key since lists are not hashable
            res[tuple(count)].append(s)
        
        return list(res.values())  # convert dict_values to list