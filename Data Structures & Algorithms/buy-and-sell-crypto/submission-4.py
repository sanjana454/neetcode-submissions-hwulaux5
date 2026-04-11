class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0  # buy pointer (tracks lowest price candidate)
        r = 1  # sell pointer (current day to sell)
        
        maxP = 0  # stores maximum profit found so far

        # move sell pointer through entire array
        while r < len(prices):

            # case 1: we have a profitable transaction
            if prices[l] < prices[r]:
                # profit = sell price - buy price
                profit = prices[r] - prices[l]

                # update maximum profit
                maxP = max(maxP, profit)

            else:
                # case 2: found a lower price
                # update buy pointer to this lower price
                l = r

            # always move sell pointer forward
            r += 1

        return maxP