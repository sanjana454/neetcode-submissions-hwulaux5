class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        
        # prices[i] = minimum cost to reach node i
        # initialize all costs as infinity
        prices = [float("inf")] * n
        
        # cost to reach source is 0
        prices[src] = 0

        # we relax edges k+1 times
        # because k stops = k+1 edges allowed
        for _ in range(k + 1):

            # make a copy to prevent using updated values in same iteration
            # (important for Bellman-Ford correctness)
            temp = prices.copy()

            # go through every flight (edge)
            for u, v, w in flights:

                # if we cannot reach u yet, skip
                if prices[u] == float("inf"):
                    continue

                # check if going from u → v gives cheaper cost
                if prices[u] + w < temp[v]:
                    temp[v] = prices[u] + w

            # update prices after this round of relaxation
            prices = temp

        # if destination still infinity → not reachable
        return prices[dst] if prices[dst] != float("inf") else -1