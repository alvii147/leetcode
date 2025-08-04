class Solution:
    def factorial(self, n: int) -> int:
        """
        Compute factorial of n recursively.
        """
        if n < 2:
            return 1

        return n * self.factorial(n - 1)

    def factorial_over_factorial(self, n: int, m: int) -> int:
        """
        Computes n! / m!, where n >= m taking advantage of the fact that
        n! / m! = n x (n - 1) x (n - 2) x ... x (m + 2) x (m + 1).
        """
        f = 1
        for i in range(m + 1, n + 1):
            f *= i

        return f

    def uniquePaths(self, m: int, n: int) -> int:
        # At each point, we can either go down or right.
        # Since we move from top left to bottom right,
        # there must be a total of m - 1 down movements and
        # n - 1 right movements. This means, the number of
        # unique paths is simply the number of permutations
        # of down and right movements.

        # Total number of movements is m + n - 2 (m - 1 down, n - 1 right).
        # So number of total permutations is (m + n - 2)!.
        # However, the order of down movements doesn't matter,
        # so we can divide this by (m - 1)!. Similarly, the order of
        # right movements doesn't matter, so we can divide this
        # by (n - 1)!, giving us the total number of unique paths of
        # (m + n - 2)! / ((m - 1)! x (n - 1)!).

        return self.factorial_over_factorial(m + n - 2, m - 1) // self.factorial(n - 1)
