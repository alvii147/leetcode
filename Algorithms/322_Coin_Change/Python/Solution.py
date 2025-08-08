class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # list of amounts and the fewest number of coins needed to make those amounts
        fewestCoins = [-1] * (amount + 1)
        # hardcode zero, as we don't need any coins to make up an amount of zero
        fewestCoins[0] = 0

        # iterate over each coin
        for coin in coins:
            # iterate over all amounts starting from current coin amount to target amount
            for a in range(coin, amount + 1):
                if fewestCoins[a - coin] < 0:
                    continue

                # if current amount can be made up with fewer coins using current coin
                # then update the fewest number of coins value for current amount
                if fewestCoins[a] < 0 or fewestCoins[a] > fewestCoins[a - coin] + 1:
                    fewestCoins[a] = fewestCoins[a - coin] + 1

        return fewestCoins[amount]
