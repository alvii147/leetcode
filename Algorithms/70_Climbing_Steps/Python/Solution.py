class Solution:
    def climbStairs(self, n: int) -> int:
        # handle initial case of 1
        if n == 1:
            return 1

        # number of ways we can reach previous previous step
        # we can reach the first step using only one way
        previous_previous_n_steps = 1
        # number of ways we can reach previous step
        # we can reach the second step by doing 2 single steps, or 1 double step
        previous_n_steps = 2

        for _ in range(2, n):
            # we can reach the current step from the previous step by adding a single step
            # or we can reach the current step from the previous previous step by adding a double step
            previous_n_steps, previous_previous_n_steps = previous_n_steps + previous_previous_n_steps, previous_n_steps

        return previous_n_steps
