from typing import List


class Price:
    def find_min_price(self, index: int, prices: List[int]) -> int:
        min_price = prices[index]
        for i in range(index, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] > min_price:
                return i - 1
        return i

    def find_max_price(self, index: int, prices: List[int]) -> int:
        max_price = prices[index]
        for i in range(index, len(prices)):
            if prices[i] > max_price:
                max_price = prices[i]
            if prices[i] < max_price:
                return i - 1
        return i

    def maxProfit(self, prices: List[int]) -> int:

        index1 = 0
        index2 = 0
        profit = 0

        while index1 < len(prices) - 1 and index2 < len(prices) - 1:
            index1 = self.find_min_price(index2, prices)
            index2 = self.find_max_price(index1, prices)
            profit = profit + (prices[index2] - prices[index1])

        return profit


aaa = Price()
aaa.maxProfit([1, 2, 3])
