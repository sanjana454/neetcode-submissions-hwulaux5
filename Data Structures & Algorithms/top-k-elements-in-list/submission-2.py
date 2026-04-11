class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Hashmap to count frequency of each number
        count = {}
        
        # Step 2: Build frequency map (num -> count)
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Step 3: Create buckets where index = frequency
        # freq[i] will store all numbers that appear i times
        freq = [[] for i in range(len(nums) + 1)]
        
        # Step 4: Place numbers into corresponding frequency bucket
        for n, c in count.items():
            freq[c].append(n)
        
        # Step 5: Collect results starting from highest frequency
        res = []
        
        # Traverse buckets from high frequency to low frequency
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                
                # Stop once we have k elements
                if len(res) == k:
                    return res