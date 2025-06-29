class Solution:
    def coalesce(self, *args: int | None) -> int | None:
        '''
        Get first integer that is not None.
        '''
        for arg in args:
            if arg is not None:
                return arg

        return None

    def getMinNotNone(self, *args: int | None) -> int | None:
        '''
        Get minimum integer that is not None.
        '''
        minVal = None
        for arg in args:
            if arg is None:
                continue

            if minVal is None:
                minVal = arg
                continue

            minVal = min(minVal, arg)

        return minVal

    def getMaxNotNone(self, *args: int | None) -> int | None:
        '''
        Get maximum integer that is not None.
        '''
        maxVal = None
        for arg in args:
            if arg is None:
                continue

            if maxVal is None:
                maxVal = arg
                continue

            maxVal = max(maxVal, arg)

        return maxVal

    def maxProduct(self, nums: List[int]) -> int:
        # keep track of local minimum and maximum
        localMinProd = None
        localMaxProd = None
        # global maximum product
        maxProd = None

        for num in nums:
            # get product of local minimum and current number
            prodWithLocalMin = num * self.coalesce(localMaxProd, 1)
            # get product of local maximum and current number
            prodWithLocalMax = num * self.coalesce(localMinProd, 1)

            # get minimum between current number, local minimum and local maximum
            localMinProd = self.getMinNotNone(num, prodWithLocalMax, prodWithLocalMin)
            # get maximum between current number, local minimum and local maximum
            localMaxProd = self.getMaxNotNone(num, prodWithLocalMax, prodWithLocalMin)

            # keep track of global maximum
            maxProd = self.getMaxNotNone(maxProd, localMaxProd)

        return maxProd
