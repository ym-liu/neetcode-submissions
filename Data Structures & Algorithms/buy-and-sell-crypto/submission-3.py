class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = sys.maxsize
        maxProfit = 0

        # iterate, considerating prices[i] as selling price
        for price in prices:
            maxProfit = max(maxProfit, price - minPrice)
            minPrice = min(minPrice, price)

        return maxProfit
